from api.incident import incidents_bp
from flask import jsonify
from api.auth.utilities import protected, check_is_admin
from api.incident.controller import post_incident,\
                                    fetch_all_incidents, fetch_an_incident,\
                                    edit_location_of_incident,\
                                    edit_comment_of_incident,\
                                    delete_incident, change_status


# Post incident route
@incidents_bp.route('/incidents', methods=['POST'])
@protected
def post(current_user):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'Access denied'}), 403
    return post_incident(current_user)


# fetch all incidents route
@incidents_bp.route('/incidents', methods=['GET'])
@protected
def get_all_incidents(current_user):
    return fetch_all_incidents()


# fetch a specific incident route
@incidents_bp.route('/incidents/<incident_id>', methods=['GET'])
@protected
def get_an_incident(curreent_user, incident_id):
    return fetch_an_incident(incident_id)


# Update incident location route
@incidents_bp.route('/incidents/<incident_id>/incident_location',
                    methods=['PATCH'])
@protected
def edit_incident_location(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'Access denied'}), 403
    return edit_location_of_incident(incident_id)


# Update incident comment route
@incidents_bp.route('/incidents/<incident_id>/incident_comment',
                    methods=['PATCH'])
@protected
def edit_incident_comment(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'Access denied'}), 403
    return edit_comment_of_incident(incident_id)


# Delete incident route
@incidents_bp.route('/incidents/<incident_id>', methods=['DELETE'])
@protected
def delete_incident_record(current_user, incident_id):
    if check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'Access denied'}), 403
    return delete_incident(incident_id)


# change incident status route
@incidents_bp.route('/incidents/<incident_id>/status', methods=['PATCH'])
@protected
def change_incident_status(current_user, incident_id):
    if not check_is_admin(current_user):
        return jsonify({'status': 403,
                        'error': 'Access denied'}), 403
    return change_status(incident_id)
