from tests.base import BaseTest
from api.incident import views
from api.incident.models import incident_db
import json


class IncidentTestCase(BaseTest):
    def test_returns_error_if_the_record_type_is_invalid(self):
        data = {
                "type":"",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A required field is either missing or empty")
        data = {
                "type":"red",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "type must a string and must be red-flag or intervention")
        data = {
                "type":9,
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "type must a string and must be red-flag or intervention")

    def test_return_error_if_location_is_invalid(self):
        data = {
                "type":"red-flag",
                "location":"2222222",
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                } 
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Location field only takes in a list of valid Lat and Long cordinates")

    def test_returns_error_if_comment_is_not_valid(self):
        data = {
                "type":"red-flag",
                "location":[3333.33, 444.1],
                "comment": 99,
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "comment must be a string")

    def test_returns_error_if_image_url_or_title_is_invalid(self):
        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"trytle":"sassaqwqwq","url":"sasasdsdd"},
            "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Image url or title or video url or title is invalid")

        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","ul":"sasasdsdd"},
            "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Image url or title or video url or title is invalid")

        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"trytle":"sassaqwqwq","rl":"sasasdsdd"},
            "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Image url or title or video url or title is invalid")

        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":10},
            "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Image url or title or video url or title is invalid")

    def test_returns_error_video_url_or_title_is_invalid(self):
        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"ti":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Image url or title or video url or title is invalid")

        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":8,"url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Image url or title or video url or title is invalid")

    def test_returns_error_if_unauthorised_user_tries_to_post_record(self):
        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_admin()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,403)
        self.assertEqual(response_data['status'], 403)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Access denied")

    def test_posts_incident_record(self):
        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)
        self.assertIn("the pot holes are many", str(response_data['data']))
        self.assertEqual(response_data['message'], "created red-flag record successfuly")

    def test_returns_all_incident_records(self):
        data = {
            "type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = {'token':self.get_token_user()})
        res = self.app.get('/api/v1/incidents', headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("the pot holes are many", str(response_data['data']))

    def test_returns_error_if_the_incident_db_is_empty(self):
        res = self.app.get('/api/v1/incidents', headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("No incidents recorded yet", str(response_data['message']))


    def test_returns_error_id_incident_record_not_found(self):
        record = {
                "incident_id":1,
                "type":"red-flag",
                "location":[3333.33, 444.1],
                "comment": "the pot holes are many",
                "image":{"title":"sassaqwqwq","url":"sasasa"},
                "video":{"title":"the Meg","url":"sasasdsdd"}
                }
        incident_db.append(record)
        print(incident_db)
        res = self.app.get('/api/v1/incidents/1', headers = {'token':self.get_token_user()})
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertIn("incident record not found", str(response_data['message']))
