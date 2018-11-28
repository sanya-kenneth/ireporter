from flask import request, jsonify, current_app as app
from api.auth.models import user_db
from functools import wraps
import re
import jwt


class validateUser:
    @staticmethod
    def validate_names(name):
        return isinstance(name, str) and not re.search(r'[\s]', name)

    @staticmethod
    def validate_phoneNumber(number):
        return isinstance(number, int)

    @staticmethod
    def validate_password(password):
        return isinstance(password, str) and len(password) >= 8 and \
                re.search(r'[A-Z]', password) and re.search(r'[0-9]', password)


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return jsonify({'status': 401, 'error': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET'],
                              algorithms=['HS256'])
            for user_info in user_db:
                if user_info['email'] == data['user']:
                    current_user = user_info
        except:
            return jsonify({'status': 401, 'error': 'Token is invalid'}), 401
        # try:
        return f(current_user, *args, **kwargs)
        # except:
        #     return jsonify({'status': 401, 'error': 'Please login first'}), 401
    return decorated


def check_is_admin(current_user):
    return current_user['isAdmin']
