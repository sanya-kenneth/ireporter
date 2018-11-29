from api.incident.models import incident_db
from api.auth.models import user_db
from api import create_app
import unittest
import json


class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        This method helps setup tests.
        It also initialises the test_client where tests will be run 
        """
        self.app = create_app('Testing')
        self.app = self.app.test_client()

    def tearDown(self):
        user_db.clear()
        incident_db.clear()

    def get_token_admin(self):
        admin_data = {
                    "firstname":"kenneth",
                    "lastname":"sanya",
                    "othernames":"ken",
                    "email":"sanya@gmail.com",
                    "phonenumber":256706578719,
                    "username":"skimo",
                    "password":"qs1szwwwaAwx"
                    }
        admin_data_login = {
                            "email":"sanya@gmail.com",
                            "password": "qs1szwwwaAwx"
                            }
        self.app.post('/api/v1/users/admin', content_type="application/json", data=json.dumps(admin_data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(admin_data_login))
        data = json.loads(res.data.decode())
        return data['access_token']


    def get_token_user(self):
        user_data = {
                    "firstname":"len",
                    "lastname":"leno",
                    "othernames":"ken",
                    "email":"len@gmail.com",
                    "phonenumber":256786578719,
                    "username":"len",
                    "password":"1awQdddddd"
                    }
        user_data_login = {
                            "email":"len@gmail.com",
                            "password": "1awQdddddd"
                            }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(user_data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(user_data_login))
        data = json.loads(res.data.decode())
        return data

    def user_header(self):
        return { 'content_type':"application/json",'Authorization':
                 'Bearer ' + self.get_token_user()['access_token']}

    def admin_header(self):
        return {'content_type':"application/json", 'Authorization':
        'Bearer ' + self.get_token_admin()}



if __name__ == '__main__':
    unittest.main()
