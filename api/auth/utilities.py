from flask import jsonify
from api.auth.models import user_db
from functools import wraps
from flask_jwt_extended import get_jwt_identity
import re


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
        return isinstance(password, str) and len(password) >= 8 and \
                re.search(r'[A-Z]', password) and re.search(r'[0-9]', password)


def get_user(current_user):
    """function returns data attached to the current user """
    for user in user_db:
        if user['email'] == current_user:
            return user


def check_is_admin(current_user):
    """function checks if a user is an admin """
    return current_user['isAdmin'] == True


def user_identity():
    current_user = get_jwt_identity()
    current_user = get_user(current_user)
    return current_user
