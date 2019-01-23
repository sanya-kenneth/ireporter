from flask import request, jsonify
from api.auth.utilities import protected_route
from api.incident.models import Incident
from api.incident.utilities import validateIncident
from api.database.db import db_handler
import json


incident_records = []


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
    current_user = user_identity()
    incident = Incident(current_user[0], incident_type, location, image, video, comment)
    db_handler().add_incident_record(incident.createdOn, incident.createdBy, incident.record_type,\
    incident.location, incident.Images['title'], incident.Images['url'], incident.Videos['title'],\
    incident.Videos['url'], incident.comment, incident.status)
    data_dict = {
        "createdon": incident.createdOn,
        "record_type": incident.record_type,
        "incident_location": incident.location,
        "image": {"title": incident.Images['title'], "url": incident.Images['url']},
        "video": {"title": incident.Videos['title'], "url": incident.Videos['url']},
        "comment": incident.comment,
        "status": incident.status
        }
    return jsonify({
                    'status': 201, 'data': data_dict,
                    'message': f'created {incident_type} record successfuly'}), 201


# function for getting all incidents
def fetch_all_incidents():
    fetched_data = db_handler().select_all_records('incident_table')
    if not fetched_data:
        return jsonify({'status': 200,
                        'message': 'No incidents recorded yet'}), 200
    keys = ["incidentid", "createdon", "createdby", "record_type",
             "incident_location",  "image", "video", "comment", "status"]
    for data in fetched_data:
        image = {"title": data[5], "url": data[6]}
        video = {"title": data[7], "url": data[8]}
        records = [data[0], data[1], data[2], data[3], data[4],
        image, video, data[9], data[10]]
        incident_records.append(dict(zip(keys, records)))
    return jsonify({ 'data': incident_records, 'status': 200}), 200


# function for getting a single incident
def fetch_an_incident(incident_id):
    try:
        incidentId = int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    record_data = db_handler().select_one_incident_record(incidentId)
    if record_data:
        data_dict = {
                "incidentid": record_data[0],
                 "createdon": record_data[1],
                 "createdby": record_data[2],
                 "record_type": record_data[3],
                 "incident_location": record_data[4],
                 "image": {"title": record_data[5], "url": record_data[6]},
                 "video": {"title": record_data[7], "url": record_data[8]},
                 "comment": record_data[9],
                 "status": record_data[10]
                }
        return jsonify({'data': data_dict,
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
    incident_data_fetch = db_handler().select_one_incident_record(incident_Id)
    if not incident_data_fetch:
        return jsonify({'status': 200,
                    'message': 'incident record not found'}), 200
    if incident_data_fetch[10] != 'Draft':
        return jsonify({'status': 400,
                        'error': 'You cannot change the location while the incident status is not Draft'}), 400
    db_handler().update_incident_record('incident_location', incident_Id, location)
    incident_record_type = incident_data_fetch[3]
    incident_data_fetch = db_handler().select_one_incident_record(incident_Id)
    data_dict = {
            "incidentid": incident_data_fetch[0],
            "createdon": incident_data_fetch[1],
            "createdby": incident_data_fetch[2],
            "record_type": incident_data_fetch[3],
            "incident_location": incident_data_fetch[4],
            "image": {"title": incident_data_fetch[5], "url": incident_data_fetch[6]},
            "video": {"title": incident_data_fetch[7], "url": incident_data_fetch[8]},
            "comment": incident_data_fetch[9],
            "status": incident_data_fetch[10]
            }
    return jsonify({'status': 200, 'data': data_dict,
                    'message': f"Updated {incident_record_type} record's location"
                    }), 200


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
    incident_result = db_handler().select_one_incident_record(incident_Id)
    if not incident_result:
        return jsonify({'status': 200,
                   'message': 'incident record not found'}), 200
    if incident_result[10] != 'Draft':
        return jsonify({'status': 400,
                        'error': 'You cannot change the location while the incident status is not Draft'}), 400
    db_handler().update_incident_record('comment', incident_Id, comment)
    incident_type = incident_result[3]
    incident_result = db_handler().select_one_incident_record(incident_Id)
    data_dict = {
            "incidentid": incident_result[0],
            "createdon": incident_result[1],
            "createdby": incident_result[2],
            "record_type": incident_result[3],
            "incident_location": incident_result[4],
            "image": {"title": incident_result[5], "url": incident_result[6]},
            "video": {"title": incident_result[7], "url": incident_result[8]},
            "comment": incident_result[9],
            "status": incident_result[10]
            }
    return jsonify({'status': 200, 'data': data_dict,
                    'message': f"Updated {incident_type} record's comment"}), 200


# function for deleting an incident
def delete_incident(incident_id):
    try:
        incident_Id = int(incident_id)
    except:
        return jsonify({'status': 400,
                        'error': 'incident_id must be a valid number'}), 400
    delete_data = db_handler().select_one_incident_record(incident_Id)
    if not delete_data:
        return jsonify({'status': 200,
                        'message': 'incident record not found'}), 200
    db_handler().delete_incident_record(incident_Id)
    return jsonify({'status': 200,
                    'message': f"{delete_data[3]} record has been deleted"}), 200


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
    incident_record_data = db_handler().select_one_incident_record(incident_Id)
    if not incident_record_data:
        return jsonify({'status': 200,
                        'message': 'incident record not found'}), 200
    db_handler().update_incident_record('incident_status', incident_Id, status)
    incident_record_data = db_handler().select_one_incident_record(incident_Id)
    data_dict = {
        "incidentid": incident_record_data[0],
        "createdon": incident_record_data[1],
        "createdby": incident_record_data[2],
        "record_type": incident_record_data[3],
        "incident_location": incident_record_data[4],
        "image": {"title": incident_record_data[5], "url": incident_record_data[6]},
        "video": {"title": incident_record_data[7], "url": incident_record_data[8]},
        "comment": incident_record_data[9],
        "status": incident_record_data[10]
        }
    return jsonify({'status': 200, 'data': data_dict,
                    'message': f"{incident_record_data[3]} record's status was successfuly updated"}), 200
