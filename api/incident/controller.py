from flask import request, jsonify
from api.auth.utilities import get_user
from api.incident.models import Incident, incident_db
from api.incident.utilities import validateIncident
from flask_jwt_extended import get_jwt_identity
import json


# function for posting an incident
def post_incident():
    details = request.get_json()
    incident_type = details.get('incident_type')
    location = details.get('location')
    comment = details.get('comment')
    image = details.get('image')
    video = details.get('video')
    if not incident_type or not location or not comment or not image\
         or not video:
        return jsonify({'status': 400,
                        'error': 'A required field is either missing or empty'
                        }), 400
    if not validateIncident.validate_type(incident_type):
        return jsonify({'status': 400,
                        'error':'type must a string and must be red-flag or intervention'}), 400
    if not validateIncident.validate_location(location):
        return jsonify({'status': 400,
                        'error': 'Location field only takes in a list of valid Lat and Long cordinates'
                        }), 400
    if not validateIncident.validate_comment(comment):
        return jsonify({'status': 400,
                        'error': 'comment must be a string'}), 400
    if not isinstance(image, dict) or not isinstance(video, dict) or not\
            validateIncident.validate_images_and_video(image) or not\
            validateIncident.validate_images_and_video(video):
        return jsonify({'status': 400,
                        'error': 'Image url or title or video url or title is invalid'}), 400
    current_user = get_jwt_identity()
    current_user = get_user(current_user)
    incident = Incident(current_user['user_id'], incident_type, location, image, video, comment)
    incident_db.append(incident.to_json())
    return jsonify({'data': incident.to_json(),
                    'status': 201,
                    'message': f'created {incident_type} record successfuly'}), 201


# function for getting all incidents
def fetch_all_incidents():
    if not incident_db:
        return jsonify({'status': 200,
                        'message': 'No incidents recorded yet'}), 200
    return jsonify({'data': incident_db, 'status': 200}), 200


# function for getting a single incident
def fetch_an_incident(incident_id):
    try:
        incidentId = int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    for incident_item in incident_db:
        if int(incident_item['incident_id']) == incidentId:
            return jsonify({'data': incident_item,
                            'status': 200}), 200
    return jsonify({'status': 200,
                    'message': 'incident record not found'}), 200


# function for editing the location of an incident
def edit_location_of_incident(incident_id):
    data = request.get_json()
    location = data.get('location')
    try:
        incident_Id = int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    if not location:
        return jsonify({'status': 400,
                        'error': 'location field is empty or missing'
                        }), 400
    if not validateIncident.validate_location(location):
        return jsonify({'status': 400,
                        'error': 'Location field only takes in a list of valid Lat and Long cordinates'
                        }), 400
    for incident_record in incident_db:
        if int(incident_record['incident_id']) == incident_Id:
            if incident_record['status'] != 'Draft':
                return jsonify({'status': 400,
                                'error': 'You cannot change the location while the incident status is not Draft'}), 400
            incident_record['location'] = location
            incident_record_type = incident_record['incident_type']
            return jsonify({'status': 200, 'data': incident_record,
                            'message': f"Updated {incident_record_type} record's location"
                            }), 200
    return jsonify({'status': 200,
                    'message': 'incident record not found'}), 200


# function for editing the comment of an incident 
def edit_comment_of_incident(incident_id):
    info = request.get_json()
    comment = info.get('comment')
    try:
        incident_Id = int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    if not comment:
        return jsonify({'status': 400,
                        'error': 'comment field is empty or missing'
                        }), 400
    if not validateIncident.validate_comment(comment):
        return jsonify({'status': 400,
                        'error': 'comment must be a string'}), 400
    for search_incident in incident_db:
        if search_incident['incident_id'] == incident_Id:
            if search_incident['status'] != 'Draft':
                return jsonify({'status': 400,
                                'error': 'You cannot change the location while the incident status is not Draft'}), 400
            search_incident['comment'] = comment
            search_incident_type = search_incident['incident_type']
            return jsonify({'status': 200, 'data': search_incident,
                           'message': f"Updated {search_incident_type} record's comment"}), 200
    return jsonify({'status': 200,
                   'message': 'incident record not found'}), 200


# function for deleting an incident
def delete_incident(incident_id):
    try:
        incident_Id = int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    for incident_data in incident_db:
        if int(incident_data['incident_id']) == incident_Id:
            incident_db.remove(incident_data)
            return jsonify({'status': 200, 'data': incident_data,
                            'message': f"{incident_data['incident_type']} record has been deleted"}), 200
    return jsonify({'status': 200,
                   'message': 'incident record not found'}), 200


# function for changing the status of an incident
def change_status(incident_id):
    status_data = request.get_json()
    status = status_data.get('status')
    try:
        incident_Id = int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    if not status:
        return jsonify({'status': 400,
                        'error': 'status field is either empty or missing'
                        }), 400
    if not validateIncident.validate_status(status):
        return jsonify({'status': 400,
                        'error': 'status must a string and must be under investigation or rejected or resolved'}), 400
    for incident_item in incident_db:
        if incident_item['incident_id'] == incident_Id:
            incident_item['status'] = status
            return jsonify({'status': 200, 'data': incident_item,
                            'message': f"{incident_item['incident_type']} record's status was successfuly updated"}), 200
    return jsonify({'status': 200,
                   'message': 'incident record not found'}), 200
