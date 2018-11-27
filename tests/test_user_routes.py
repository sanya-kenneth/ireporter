from tests.base import BaseTest
from api.auth import views
import json


class UserTestCase(BaseTest):
    def test_returns_error_if_firstname_is_not_valid(self):
        data = {	
            "firstname":"",
            "lastname":"sanya",
            "othernames":"ken",
            "email":"sanya@gmail.com",
            "phonenumber":25676578719,
            "username":"skimo",
            "password":"ssq1waAwx"
            }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "A required field is either missing or empty")