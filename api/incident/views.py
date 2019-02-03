from api.incident import incidents_bp
from flask import jsonify
from api.auth.utilities import check_is_admin, protected_route, \
    restrict_admin_access, restrict_normal_user_access
from api.incident.controller import fetch_all_incidents, fetch_an_incident,\
    edit_location_of_incident,\
    edit_comment_of_incident,\
    delete_incident, change_status, post_incident
from api.database.db import db_handler


# Post red-flags and intervention routes
@incidents_bp.route('/red-flags', methods=['POST'])
@incidents_bp.route('/interventions', methods=['POST'])
@protected_route
@restrict_admin_access
def post(current_user):
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
@restrict_admin_access
def edit_incident_location(current_user, incident_id):
    check_record = db_handler().select_one_record('incident_table', 'incidentid',
                                                  incident_id)
    if check_record:
        if int(check_record[2]) != current_user[0]:
            return jsonify({'status': 403,
                            'error': 'You can only edit the location of a record you created'
                            }), 403
    return edit_location_of_incident(incident_id, 'red-flag')


# Update intervention location route
@incidents_bp.route('/interventions/<incident_id>/incident_location',
                    methods=['PATCH'])
@protected_route
@restrict_admin_access
def edit_intervention_location(current_user, incident_id):
    check_record = db_handler().select_one_record('incident_table', 'incidentid',
                                                  incident_id)
    if check_record:
        if int(check_record[2]) != current_user[0]:
            return jsonify({'status': 403,
                            'error': 'You can only edit the location of a record you created'
                            }), 403
    return edit_location_of_incident(incident_id, 'intervention')


# Update incident comment route
@incidents_bp.route('/red-flags/<incident_id>/incident_comment',
                    methods=['PATCH'])
@protected_route
@restrict_admin_access
def edit_redflag_comment(current_user, incident_id):
    record_data = db_handler().select_one_record('incident_table', 'incidentid',
                                                 incident_id)
    if record_data:
        if int(record_data[2]) != current_user[0]:
            return jsonify({'status': 403,
                            'error': 'You can only edit the location of a record you created'
                            }), 403
    return edit_comment_of_incident(incident_id, 'red-flag')


# Update intervention comment
@incidents_bp.route('/interventions/<incident_id>/incident_comment',
                    methods=['PATCH'])
@protected_route
@restrict_admin_access
def edit_intervention_comment(current_user, incident_id):
    update_data = db_handler().select_one_record('incident_table', 'incidentid',
                                                 incident_id)
    if update_data:
        if int(update_data[2]) != current_user[0]:
            return jsonify({'status': 403,
                            'error': 'You can only edit the location of a record you created'
                            }), 403
    return edit_comment_of_incident(incident_id, 'intervention')


# Delete red-flag route
@incidents_bp.route('/red-flags/<incident_id>', methods=['DELETE'])
@protected_route
@restrict_admin_access
def delete_red_flag_record(current_user, incident_id):
    delete = db_handler().select_one_incident('incident_table', 'incidentid',
                                              incident_id, 'red-flag')
    if delete:
        if int(delete[2]) != current_user[0]:
            return jsonify({'status': 403,
                            'error': 'You can only delete a record you created'
                            }), 403
    return delete_incident(incident_id, 'red-flag')


# Delete intervention route
@incidents_bp.route('/interventions/<incident_id>', methods=['DELETE'])
@protected_route
@restrict_admin_access
def delete_intervention_record(current_user, incident_id):
    delete_data = db_handler().select_one_incident('incident_table', 'incidentid',
                                                   incident_id, 'intervention')
    if delete_data:
        if int(delete_data[2]) != current_user[0]:
            return jsonify({'status': 403,
                            'error': 'You can only delete a record you created'
                            }), 403
    return delete_incident(incident_id, 'intervention')


# change incident status route
@incidents_bp.route('/red-flags/<incident_id>/status', methods=['PATCH'])
@protected_route
@restrict_normal_user_access
def change_redflag_status(current_user, incident_id):
    return change_status(incident_id, 'red-flag')


@incidents_bp.route('/interventions/<incident_id>/status', methods=['PATCH'])
@protected_route
@restrict_normal_user_access
def change_intervention_status(current_user, incident_id):
    return change_status(incident_id, 'intervention')
