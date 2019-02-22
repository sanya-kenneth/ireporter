from flask import request, jsonify
from validate_email import validate_email
from api.auth.models import User
from api.auth.utilities import validateUser, encode_token
from werkzeug.security import generate_password_hash, check_password_hash
from api.database.db import db_handler


user_list = []


# function to signup a user
def signup_user():
    data = request.get_json()
    firstName = data.get('firstname')
    lastName = data.get('lastname')
    otherNames = data.get('othernames')
    email = data.get('email')
    phoneNumber = data.get('phonenumber')
    userName = data.get('username')
    userPassword = data.get('password')
    if not firstName or not lastName or not\
            otherNames or not email or not phoneNumber or not \
            userName or not userPassword:
        return jsonify({'status': 400,
                        'error': 'A required field is either missing or empty'
                        }), 400
    if not validateUser.validate_names(firstName) or not \
            validateUser.validate_names(lastName) or not \
            validateUser.validate_names(otherNames) or not \
            validateUser.validate_names(userName):
        return jsonify({'status': 400,
                        'error': 'Name must be a string and must not contain spaces'
                        }), 400
    if not validateUser.validate_phoneNumber(phoneNumber):
        return jsonify({'status': 400,
                        'error': 'Only numbers are allowed for the phonenumber field'
                        }), 400
    if not validate_email(email):
        return jsonify({'status': 400, 'error': 'Invalid email'}), 400
    if not validateUser.validate_password(userPassword):
        return jsonify({'status': 400,
                        'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'}), 400
    user = User(firstName, lastName, otherNames, email,
                phoneNumber, userName, generate_password_hash(userPassword))
    if db_handler().select_one_record('user_table', 'useremail', email):
        return jsonify({'status': 400,
                        'error': 'User account already exists'}), 400
    user = db_handler().add_user(user.firstname, user.lastname, user.othernames,
                                 user.username, user.email, user.phoneNumber,
                                 user.password, user.registered, user.isAdmin)
    data.pop('password')
    return jsonify({'status': 201, 'data': data,
                    'message': 'Your Account was created successfuly'
                    }), 201


# function to login a user
def login_user():
    login_info = request.get_json()
    login_email = login_info.get('email')
    login_password = login_info.get('password')
    if not login_email or not login_password:
        return jsonify({'status': 400,
                        'error': 'email or password cannot be empty'}), 400
    if not validate_email(login_email):
        return jsonify({'status': 400, 'error': 'Invalid email'}), 400
    if not validateUser.validate_password(login_password):
        return jsonify({'status': 400,
                        'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'
                        }), 400
    user_data = db_handler().select_one_record(
        'user_table', 'useremail', login_email)
    if user_data:
        if user_data[5] == login_email and \
                check_password_hash(user_data[7], login_password):
            access_token = encode_token(login_email, user_data[9])
            return jsonify({'status': 200, 'access_token': access_token.decode('UTF-8'),
                            'message': 'You are now loggedin', 'user_role': user_data[9]}), 200
    return jsonify({'status': 401, 'error': 'Wrong email or password'}), 401


def get_all_users(current_user):
    if current_user[9] is False:
        return jsonify({'status': 403,
                        'error': 'You are not allowed to perform this action'}), 403
    all_users = db_handler().get_all_users()
    if not all_users:
        return jsonify({'status': 200,
                        'message': 'There no users registered yet'}), 200
    user_keys = ["userid", "firstname", "lastname", "othernames", "username",
    "useremail", "phonenumber", "Joined", "User type"]
    user_list = []
    for user in all_users:
        user_details = [user[0], user[1], user[2], user[3], user[4], user[5],
        user[6], user[8], user[9]]
        user_list.append(dict(zip(user_keys, user_details)))
    user_list.reverse()
    return jsonify({'data': user_list, 'status': 200}), 200


