from api.auth import auths
from api.auth.controller import signup_user, login_user
from flask import make_response, jsonify


# signup user route
@auths.route('/users', methods=['POST'])
def signup():
   return signup_user()


# login user or admin route
@auths.route('/users/login', methods=['POST'])
def login():
   return login_user()


# custom error handler
@auths.app_errorhandler(400)
def bad_request(error):
    """ Customise HTTP 400 Bad request error to return custom message
        when ever an HTTP error 400 is raised.
    """
    return make_response(jsonify({'status': 400,
                                  'error': ' :( Bad Request'})), 400
