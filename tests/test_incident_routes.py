from tests.base import BaseTest
from api.incident import views
from api.incident.models import incident_db
import json


class IncidentTestCase(BaseTest):
    def test_returns_error_if_the_record_type_is_empty(self):
        data = {
                "incident_type":"",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)

    def test_returns_error_if_the_record_type_is_invalid(self):
        data = {
                "incident_type":"red",
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        
    def test_returns_error_if_the_record_type_is_not_a_string(self):
        data = {
                "incident_type":9,
                "location":[3333.33, 444.1],
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_return_error_if_location_is_invalid(self):
        data = {
                "incident_type":"red-flag",
                "location":"2222222",
                "comment": "its terrible",
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                } 
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        
    def test_returns_error_if_comment_is_not_valid(self):
        data = {
                "incident_type":"red-flag",
                "location":[3333.33, 444.1],
                "comment": 99,
                "image":{"title":"sassaqwqwq","url":"sasasdsdd"},
                "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
                }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)

    def test_returns_error_if_image_title_is_invalid(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"trytle":"sassaqwqwq","url":"sasasdsdd"},
            "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
    
    def test_returns_error_if_image_url_is_invalid(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","ul":"sasasdsdd"},
            "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)

    def test_returns_error_if_image_url_data_is_invalid(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":10},
            "video":{"title":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)

    def test_returns_error_video_title_is_invalid(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"ti":"sassaqwqwq","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)

    def test_returns_error_video_title_data_is_invalid(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":8,"url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 400)

    def test_returns_error_if_unauthorised_user_tries_to_post_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.admin_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,403)

    def test_posts_incident_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        res = self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)

    def test_returns_all_incident_records(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/incidents', headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)

    def test_returns_one_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.get('/api/v1/incidents/1', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)

    def test_returns_error_if_the_incident_db_is_empty(self):
        res = self.app.get('/api/v1/incidents', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)


    def test_returns_error_id_incident_record_not_found(self):
        record = {
                "incident_id":14,
                "incident_type":"red-flag",
                "location":[3333.33, 444.1],
                "comment": "the pot holes are many",
                "image":{"title":"sassaqwqwq","url":"sasasa"},
                "video":{"title":"the Meg","url":"sasasdsdd"}
                }
        incident_db.append(record)
        res = self.app.get('/api/v1/incidents/1', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)

    def test_edits_incident_location(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        data2 = {
                "location": [3.333, 33.3]
                }
        self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/incidents/1/incident_location', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        self.assertEqual(res.status_code, 200)

    def test_updates_incident_comment(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        data2 = {
                "comment": "This is urgent"
                }
        self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/incidents/1/incident_comment', content_type="application/json",
         data=json.dumps(data2), headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)


    def test_returns_error_if_user_tries_to_delete_record_thats_not_there(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        self.app.post('/api/v1/incidents', content_type="application/json",
            data=json.dumps(data), headers = self.user_header())
        res = self.app.delete('/api/v1/incidents/12', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)

    def test_deletes_incident_record(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        self.app.post('/api/v1/incidents', content_type="application/json",
         data=json.dumps(data), headers = self.user_header())
        res = self.app.delete('/api/v1/incidents/1', content_type="application/json",
         headers = self.user_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)

    def test_changes_incident_record_status(self):
        data = {
            "incident_type":"red-flag",
            "location":[3333.33, 444.1],
            "comment": "the pot holes are many",
            "image":{"title":"sassaqwqwq","url":"sasasa"},
            "video":{"title":"the Meg","url":"sasasdsdd"}
            }
        data2 = {
                "status": "resolved"
                }
        self.app.post('/api/v1/incidents', content_type="application/json",
         data=json.dumps(data), headers = self.user_header())
        res = self.app.patch('/api/v1/incidents/1/status', content_type="application/json",
         data=json.dumps(data2), headers = self.admin_header())
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
