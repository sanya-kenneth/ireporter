from tests.base import BaseTest
from api.auth import views
import json


class UserTestCase(BaseTest):
    def test_returns_error_if_first_name_is_not_valid(self):
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

    def test_returns_error_if_last_name_is_not_valid(self):
        data = {
            "firstname":"kenneth",
            "lastname":"",
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

    def test_returns_error_if_other_names_is_missing(self):
        data = {
            "firstname":"kenneth",
            "lastname":"sanya",
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

    def test_returns_error_if_email_is_missing(self):
        data = {
        "firstname":"kenneth",
        "lastname":"sanya",
        "othernames":"ken",
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
    
    def test_returns_error_if_first_name_contains_white_space(self):
        data = {
                "firstname":"ken neth",
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
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_first_name_is_not_a_string(self):
        data = {
                "firstname":25,
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
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_last_name_contains_white_space(self):
        data = {
                "firstname":"kenneth",
                "lastname":"san ya",
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
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_last_name_is_not_a_string(self):
        data = {
                "firstname":"kenneth",
                "lastname":24,
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
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_other_names_contains_white_space(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":" ke n ",
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
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_user_name_contains_whitespace(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":25676578719,
                "username":"ski mo",
                "password":"ssq1waAwx"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Name must be a string and must not contain spaces")

    def test_returns_error_if_phone_number_is_invalid(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":"0706578719",
                "username":"skimo",
                "password":"ssq1waAwx"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Only numbers are allowed for the phonenumber field")

    def test_returns_error_if_email_is_invalid(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanyagmail.com",
                "phonenumber":256706578719,
                "username":"skimo",
                "password":"ssq1waAwx"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Invalid email")

    def test_returns_error_if_password_is_too_short(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":256706578719,
                "username":"skimo",
                "password":"1waAwx"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
                         "Password must be atleast 8 characters and should have atleast one number and one capital letter")

    def test_returns_error_if_password_is_weak(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":256706578719,
                "username":"skimo",
                "password":"qsszwwwaAwx"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'],
                         "Password must be atleast 8 characters and should have atleast one number and one capital letter")

    def test_returns_error_if_user_already_exists(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":256706578719,
                "username":"skimo",
                "password":"qs1szwwwaAwx"
                }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))        
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code,400)
        self.assertEqual(response_data['status'], 400)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "User account already exists")

    def test_can_signup_user(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":256706578719,
                "username":"skimo",
                "password":"qs1szwwwaAwx"
                }
        res = self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 201)
        self.assertEqual(response_data['status'], 201)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'], "Your Account was created successfuly")

    def test_can_login_user(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":256706578719,
                "username":"skimo",
                "password":"qs1szwwwaAwx"
                }
        login_data = {
                       "email":"sanya@gmail.com",
                       "password": "qs1szwwwaAwx"
                     }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_data['status'], 200)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['message'], "You are now loggedin")

    def test_returns_error_on_failure_to_login(self):
        data = {
                "firstname":"kenneth",
                "lastname":"sanya",
                "othernames":"ken",
                "email":"sanya@gmail.com",
                "phonenumber":256706578719,
                "username":"skimo",
                "password":"qs1szwwwaAwx"
                }
        login_data = {
                       "email":"sanya@gmail.com",
                       "password": "qs1szwssssswwaAwx"
                     }
        self.app.post('/api/v1/users', content_type="application/json", data=json.dumps(data))
        res = self.app.post('/api/v1/users/login', content_type="application/json", data=json.dumps(login_data))
        response_data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 401)
        self.assertEqual(response_data['status'], 401)
        self.assertIsInstance(response_data, dict)
        self.assertEqual(response_data['error'], "Wrong email or password")
