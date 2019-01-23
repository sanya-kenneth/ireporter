from api.database.db import db_handler
from functools import wraps
from flask import jsonify, request, current_app as app
import re
import jwt
import datetime


class validateUser:
    """Validator class for users """
    @staticmethod
    def validate_names(name):
        """method validates user's names """
        return isinstance(name, str) and not re.search(r'[\s]', name)

    @staticmethod
    def validate_phoneNumber(number):
        """method validates user's phone number """
        return isinstance(number, int)

    @staticmethod
    def validate_password(password):
        """method validates user's password """
        return isinstance(password, str) and len(password) >= 8 and\
            re.search(r'[A-Z]', password) and re.search(r'[0-9]', password)


def check_is_admin(current_user):
    """function checks if a user is an admin """
    return current_user[9] is True


class Jwt_protect:
    def encode_token(self, user_email):
        """ 
        Generates authentication jwt token
        :param user_email:

        """
        try:
            payload = {
                # JWT expiration time
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=24),
                # issued at
                'iat': datetime.datetime.utcnow(),
                # token user info
                'sub': user_email
            }
            return jwt.encode(payload, app.config['SECRET'],
                              algorithm='HS256')
        except Exception as e:
            return e


jwt_obj = Jwt_protect()


def protected_route(f):
    """
    Decorator to protect routes
    """
    @wraps(f)
    def inner_func(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'status': 401,
                            'error': 'Token is missing'}), 401
        try:
            data = jwt.decode(
                token, app.config['SECRET'], algorithms=['HS256'])
            current_user = db_handler().select_one_user(data['sub'])
        except jwt.ExpiredSignatureError:
            return jsonify({'status': 401,
                            'error': 'Token signature expired. Please login'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'status': 401,
                            'error': 'Invalid token. Please login again'}), 401
        return f(current_user, *args, **kwargs)
    return inner_func
