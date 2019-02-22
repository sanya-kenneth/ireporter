from api.auth import auths
from api.auth.controller import signup_user, login_user,\
    get_all_users, get_one_user
from flask import make_response, jsonify
from api.database.db import db_handler
from api.auth.utilities import protected_route


# signup user
@auths.route('/users', methods=['POST'])
def signup():
    return signup_user()


# login user route
@auths.route('/users/login', methods=['POST'])
def login():
    return login_user()


# get all users route
@auths.route('/users', methods=['GET'])
@protected_route
def get_users(current_user):
    return get_all_users(current_user)

# get one user route
@auths.route('/users/<user_id>', methods=['GET'])
@protected_route
def get_a_user(current_user, user_id):
    return get_one_user(user_id)


# custom error handler
@auths.app_errorhandler(400)
def bad_request(error):
    """ Customise HTTP 400 Bad request error to return custom message
        when ever an HTTP error 400 is raised.
    """
    return make_response(jsonify({'status': 400,
                                  'error': ' :( Bad Request'})), 400
