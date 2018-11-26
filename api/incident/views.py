from api.incident import incidents_bp
from flask import request, jsonify, json
from api.incident.utilities import validateIncident
from api.incident.models import Incident


incident_db = []


@incidents_bp.route('/incidents', methods=['POST'])
def post():
    details = json.loads(request.data)
    created = details['createdby']
    type = details['type']
    location = details['location']
    comment = details['comment']
    validate_incident_data = validateIncident(created, type, location,
                                              'ssas', 'asasa', comment)
    if not created or not type or not location or not comment:
        return jsonify({'status': 400,
                        'error': 'Required field cant be empty'}), 400
    if not validate_incident_data.validate_createdBy():
        return jsonify({
                        'error': 'createdBy must be a string and must not contain spaces',
                        'status': 400}), 400
    if not validate_incident_data.validate_type():
        return jsonify({'status': 400,
                        'error': 'type must a string and must be red-flag or intervention'}), 400
    if not validate_incident_data.validate_location():
        return jsonify({'status': 400,
                        'error': 'only numbers are allowed for location field'}), 400
    if not validate_incident_data.validate_comment():
        return jsonify({'status': 400,
                        'error': 'comment must be a string'}), 400
    incident = Incident(created, type, location, 'images', 'videos', comment)
    incident_db.append(incident.to_json())
    return jsonify({'data': incident.to_json(),
                    'status': 201,
                    'message': f'created {type} record successfuly'}), 201


@incidents_bp.route('/incidents', methods=['GET'])
def get_all_incidents():
    if not incident_db:
        return jsonify({'status': 200,
                        'message': 'No incidents recorded yet'}), 200
    return jsonify({'data': incident_db, 'status': 200}), 200


@incidents_bp.route('/incidents/<incident_id>', methods=['GET'])
def get_an_incident(incident_id):
    for record in incident_db:
        if record['incident_id'] == incident_id:
            return jsonify({'data': record, 'status': 200}), 200
    return jsonify({'status': 200,
                    'message': 'incident record not found'}), 200


@incidents_bp.route('/incidents/<incident_id>/incident_location',
                    methods=['PATCH'])
def edit_incident_location(incident_id):
    data = json.loads(request.data)
    location = data['location']
    validate_incident_data = validateIncident('username',
                                              type, location, 'ssas',
                                              'asasa', 'comment')
    if not validate_incident_data.validate_location():
        return jsonify({'status': 400,
                        'error': 'only numbers are allowed for location field'}), 400
    for incident_record in incident_db:
        if incident_record['incident_id'] == incident_id:
            incident_record['location'] = location
            incident_record_type = incident_record['type']
            return jsonify({'status': 200, 'data': incident_record,
                            'message': f"Updated {incident_record_type} record's location"}), 200
    return jsonify({'status': 200,
                    'message': 'incident record not found'}), 200


@incidents_bp.route('/incidents/<incident_id>/incident_comment',
                    methods=['PATCH'])
def edit_incident_comment(incident_id):
    request_info = json.loads(request.data)
    comment = request_info['comment']
    validate_incident = validateIncident('username', type, 7231782,
                                         'url', 'url', comment)
    if not validate_incident.validate_comment():
        return jsonify({'status': 400,
                        'error': 'comment must be a string'}), 400
    for search_incident in incident_db:
        if search_incident['incident_id'] == incident_id:
            search_incident['comment'] = comment
            search_incident_type = search_incident['type']
            return jsonify({'status': 200, 'data': search_incident,
                           'message': f"Updated {search_incident_type} record's comment"}), 200
    return jsonify({'status': 200,
                   'message': 'incident record not found'}), 200


@incidents_bp.route('/incidents/<incident_id>', methods=['DELETE'])
def delete_incident_record(incident_id):
    for incident_data in incident_db:
        if incident_data['incident_id'] == incident_id:
            incident_db.remove(incident_data)
            return jsonify({'status': 200, 'data': incident_data,
                           'message': f"{incident_data['type']} record has been deleted"}), 200
    return jsonify({'status': 200,
                   'message': 'incident record not found'}), 200
