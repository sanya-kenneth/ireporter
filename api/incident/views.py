from api.incident import incidents_bp
from flask import jsonify
from api.auth.utilities import check_is_admin, protected_route
from api.incident.controller import fetch_all_incidents, fetch_an_incident,\
    edit_location_of_incident,\
    edit_comment_of_incident,\
    delete_incident, change_status, post_incident
from api.database.db import db_handler


# Post red-flags and intervention routes
@incidents_bp.route('/red-flags', methods=['POST'])
@incidents_bp.route('/interventions', methods=['POST'])
@protected_route
def post(current_user):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    return post_incident(current_user)


# fetch all red-flags route
@incidents_bp.route('/red-flags', methods=['GET'])
@protected_route
def get_all_red_flags(current_user):
    return fetch_all_incidents('red-flag')


# fetch all interventions route
@incidents_bp.route('/interventions', methods=['GET'])
@protected_route
def get_all_interventions(current_user):
    return fetch_all_incidents('intervention')


# fetch a specific red-flag route
@incidents_bp.route('/red-flags/<incident_id>', methods=['GET'])
@protected_route
def get_a_redflag(current_user, incident_id):
    return fetch_an_incident(incident_id, 'red-flag')


# fetch a specific intervention route
@incidents_bp.route('/interventions/<incident_id>', methods=['GET'])
@protected_route
def get_an_intervention(current_user, incident_id):
    return fetch_an_incident(incident_id, 'intervention')


# Update redflag location route
@incidents_bp.route('/red-flags/<incident_id>/incident_location',
                    methods=['PATCH'])
@protected_route
def edit_incident_location(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    check_record = db_handler().select_one_record('incident_table', 'incidentid',
                                                  incident_id)
    if int(check_record[2]) != current_user[0]:
        return jsonify({'status': 403,
                        'error': 'You can only edit the location of a record you created'
                        }), 403
    return edit_location_of_incident(incident_id, 'red-flag')


# Update intervention location route
@incidents_bp.route('/interventions/<incident_id>/incident_location',
                    methods=['PATCH'])
@protected_route
def edit_intervention_location(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    check_record = db_handler().select_one_record('incident_table', 'incidentid',
                                                  incident_id)
    if int(check_record[2]) != current_user[0]:
        return jsonify({'status': 403,
                        'error': 'You can only edit the location of a record you created'
                        }), 403
    return edit_location_of_incident(incident_id, 'intervention')


# Update incident comment route
@incidents_bp.route('/red-flags/<incident_id>/incident_comment',
                    methods=['PATCH'])
@protected_route
def edit_redflag_comment(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    record_data = db_handler().select_one_record('incident_table', 'incidentid',
                                                 incident_id)
    if int(record_data[2]) != current_user[0]:
        return jsonify({'status': 403,
                        'error': 'You can only edit the location of a record you created'
                        }), 403
    return edit_comment_of_incident(incident_id, 'red-flag')


# Update intervention comment
@incidents_bp.route('/interventions/<incident_id>/incident_comment',
                    methods=['PATCH'])
@protected_route
def edit_intervention_comment(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    update_data = db_handler().select_one_record('incident_table', 'incidentid',
                                                 incident_id)
    if int(update_data[2]) != current_user[0]:
        return jsonify({'status': 403,
                        'error': 'You can only edit the location of a record you created'
                        }), 403
    return edit_comment_of_incident(incident_id, 'intervention')


# Delete incident route
@incidents_bp.route('/red-flags/<incident_id>', methods=['DELETE'])
@incidents_bp.route('/interventions/<incident_id>', methods=['DELETE'])
@protected_route
def delete_incident_record(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    return delete_incident(incident_id)


# change incident status route
@incidents_bp.route('/red-flags/<incident_id>/status', methods=['PATCH'])
@incidents_bp.route('/interventions/<incident_id>/status', methods=['PATCH'])
@protected_route
def change_incident_status(current_user, incident_id):
    if not check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    return change_status(incident_id)
