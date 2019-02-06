from tests.base import BaseTest
from api.incident import views
import json


class IncidentTestCase(BaseTest):
    def test_returns_error_if_the_record_type_is_empty(self):
        data = {
                "incident_type":"",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A required field is either missing or empty")

    def test_returns_error_if_the_record_type_is_invalid(self):
        data = {
                "incident_type":"red",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "type must a string and must be red-flag or intervention")
        
    def test_returns_error_if_the_record_type_is_not_a_string(self):
        data = {
                "incident_type":9,
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "type must a string and must be red-flag or intervention")

    def test_return_error_if_location_is_invalid(self):
        data = {
                "incident_type":"red-flag",
                "location":"2222222",
                "comment": "its terrible",
                } 
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],"Location field only takes in a list of valid Lat and Long cordinates")

    def test_returns_error_if_comment_is_not_valid(self):
        data = {
                "incident_type":"red-flag",
                "location":[3333.33, 444.1],
                "comment": 99,
                }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "comment must be a string")

    def test_returns_error_if_unauthorised_user_tries_to_post_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.admin_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,403)
        self.assertEqual(response_data['status'], 403)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "You do not have permission to perform this action")

    def test_posts_incident_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        res = self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)
        self.assertIn("the pot holes are many", str(response_data['data']))
        self.assertEqual(response_data['message'], "created red-flag record successfuly")

    def test_returns_all_incident_records(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/red-flags', headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("the pot holes are many", str(response_data['data']))

    def test_returns_one_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/red-flags/1', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("the pot holes are many", str(response_data['data']))

    def test_returns_error_if_the_incident_db_is_empty(self):
        res = self.app.get('/api/v1/red-flags', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("No incidents recorded yet", str(response_data['message']))


    def test_returns_error_if_incident_record_not_found(self):
        res = self.app.get('/api/v1/red-flags/1', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("Incident record not found", str(response_data['message']))

    def test_edits_incident_location(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "location": [3.333, 33.3]
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/red-flags/1/incident_location', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("Updated red-flag record's location", response_data['message'])

    def test_updates_incident_comment(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "comment": "This is urgent"
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/red-flags/1/incident_comment', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        # print(response_data['error'])
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("Updated red-flag record's comment", response_data['message'])


    def test_returns_error_if_user_tries_to_delete_record_thats_not_there(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        self.app.post('/api/v1/red-flags', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.delete('/api/v1/red-flags/12', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("incident record not found", str(response_data['message']))

    def test_deletes_incident_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        self.app.post('/api/v1/red-flags', content_type="application/json",
         data=json.dumps(data), headers = self.user_header())
        res = self.app.delete('/api/v1/red-flags/1', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("red-flag record has been deleted", str(response_data['message']))

    def test_changes_incident_record_status(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            }
        data2 = {
                "status": "resolved"
                }
        self.app.post('/api/v1/red-flags', content_type="application/json",
         data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/red-flags/1/status', content_type="application/json",
         data=json.dumps(data2), headers = self.admin_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("red-flag record's status was successfuly updated", response_data['message'])
