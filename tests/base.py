from api import create_app
from flask import current_app as app
from api.database.db import Database
from api.auth.models import User
from werkzeug.security import generate_password_hash
import datetime
import unittest
import json


class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        This method helps setup tests.
        It also initialises the test_client where tests will be run 
        """
        self.app = create_app('Testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = Database(self.app.config['DATABASE_URI'])
        self.db.create_tables()
        self.app = self.app.test_client()
        self.create_admin()

    def tearDown(self):
        self.db.drop_tables()

    def get_token_admin(self):
        admin_data_login = {
            "email": "ken@gmail.com",
            "password": "Ken1234567"
        }
        res = self.app.post('/api/v1/users/login/admin', content_type="application/json",
                            data=json.dumps(admin_data_login))
        data = json.loads(res.data.decode())
        return data['access_token']

    def get_token_user(self):
        user_data = {
            "firstname": "len",
            "lastname": "leno",
            "othernames": "ken",
            "email": "len@gmail.com",
            "phonenumber": 256786578719,
            "username": "len",
            "password": "1awQdddddd"
        }
        user_data_login = {
            "email": "len@gmail.com",
            "password": "1awQdddddd"
        }
        self.app.post('/api/v1/users', content_type="application/json",
                      data=json.dumps(user_data))
        res = self.app.post('/api/v1/users/login', content_type="application/json",
                            data=json.dumps(user_data_login))
        data = json.loads(res.data.decode())
        return data

    def user_header(self):
        return {'content_type': "application/json", 'Authorization':
                self.get_token_user()['access_token']}

    def admin_header(self):
        return {'content_type': "application/json", 'Authorization':
                self.get_token_admin()}

    def create_admin(self):
        return self.db.add_user('ken', 'kennedy', 'kenx', 'ken', 'ken@gmail.com',
                                '0706578719', generate_password_hash(
                                    'Ken1234567'),
                                datetime.datetime.now(), isAdmin=True)


if __name__ == '__main__':
    unittest.main()
