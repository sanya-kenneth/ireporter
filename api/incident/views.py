from api.incident import incidents_bp
from flask import jsonify
from flask_jwt_extended import jwt_required
from api.auth.utilities import check_is_admin, user_identity, is_admin,\
                               check_is_loggedin
from api.incident.controller import post_incident,\
                                    fetch_all_incidents, fetch_an_incident,\
                                    edit_location_of_incident,\
                                    edit_comment_of_incident,\
                                    delete_incident, change_status


# Post incident route
@incidents_bp.route('/incidents', methods=['POST'])
@jwt_required
@check_is_loggedin
@is_admin
def post():
    return post_incident()


# fetch all incidents route
@incidents_bp.route('/incidents', methods=['GET'])
@jwt_required
@check_is_loggedin
def get_all_incidents():    
    return fetch_all_incidents()


# fetch a specific incident route
@incidents_bp.route('/incidents/<incident_id>', methods=['GET'])
@jwt_required
@check_is_loggedin
def get_an_incident(incident_id):  
    return fetch_an_incident(incident_id)


# Update incident location route
@incidents_bp.route('/incidents/<incident_id>/incident_location',
                    methods=['PATCH'])
@jwt_required
@check_is_loggedin
@is_admin
def edit_incident_location(incident_id):
    return edit_location_of_incident(incident_id)


# Update incident comment route
@incidents_bp.route('/incidents/<incident_id>/incident_comment',
                    methods=['PATCH'])
@jwt_required
@check_is_loggedin
@is_admin
def edit_incident_comment(incident_id):
    return edit_comment_of_incident(incident_id)


# Delete incident route
@incidents_bp.route('/incidents/<incident_id>', methods=['DELETE'])
@jwt_required
@check_is_loggedin
@is_admin
def delete_incident_record(incident_id):    
    return delete_incident(incident_id)


# change incident status route
@incidents_bp.route('/incidents/<incident_id>/status', methods=['PATCH'])
@jwt_required
@check_is_loggedin
def change_incident_status(incident_id):
    if not check_is_admin(user_identity()):
        return jsonify({'status': 403,
                        'error': 'Access denied'}), 403
    return change_status(incident_id)
