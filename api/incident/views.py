from api.incident import incidents_bp
from flask import jsonify
from api.auth.utilities import check_is_admin, protected_route
from api.incident.controller import fetch_all_incidents, fetch_an_incident,\
    edit_location_of_incident,\
    edit_comment_of_incident,\
    delete_incident, change_status, post_incident
from api.database.db import db_handler


# Post incident route
@incidents_bp.route('/incidents', methods=['POST'])
@protected_route
def post(current_user):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    return post_incident(current_user)


# fetch all incidents route
@incidents_bp.route('/incidents', methods=['GET'])
@protected_route
def get_all_incidents(current_user):
    return fetch_all_incidents()


# fetch a specific incident route
@incidents_bp.route('/incidents/<incident_id>', methods=['GET'])
@protected_route
def get_an_incident(current_user, incident_id):
    return fetch_an_incident(incident_id)


# Update incident location route
@incidents_bp.route('/incidents/<incident_id>/incident_location',
                    methods=['PATCH'])
@protected_route
def edit_incident_location(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    check_record = db_handler().select_one_incident_record(incident_id)
    if int(check_record[2]) != current_user[0]:
        return jsonify({'status': 403,
                        'error': 'You can only edit the location of a record you created'
                        }), 403
    return edit_location_of_incident(incident_id)


# Update incident comment route
@incidents_bp.route('/incidents/<incident_id>/incident_comment',
                    methods=['PATCH'])
@protected_route
def edit_incident_comment(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    record_data = db_handler().select_one_incident_record(incident_id)
    if int(record_data[2]) != current_user[0]:
        return jsonify({'status': 403,
                        'error': 'You can only edit the location of a record you created'
                        }), 403
    return edit_comment_of_incident(incident_id)


# Delete incident route
@incidents_bp.route('/incidents/<incident_id>', methods=['DELETE'])
@protected_route
def delete_incident_record(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    return delete_incident(incident_id)


# change incident status route
@incidents_bp.route('/incidents/<incident_id>/status', methods=['PATCH'])
@protected_route
def change_incident_status(current_user, incident_id):
    if not check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'You do not have permission to perform this action'
                        }), 403
    return change_status(incident_id)
