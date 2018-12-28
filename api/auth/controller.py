from flask import request, jsonify
from validate_email import validate_email
from api.auth.models import User, Admin, user_db
from api.auth.utilities import validateUser
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


# function to signup a user
def signup_user(user_type):
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
    if user_type == 'user':
        user = User(firstName, lastName, otherNames, email,
                    phoneNumber, userName, generate_password_hash(userPassword))
        if User.check_user_exists(email):
            return jsonify({'status': 400,
                            'error': 'User account already exists'}), 400
    elif user_type == 'admin':
        user = Admin(firstName, lastName, otherNames, email,
                     phoneNumber, userName, generate_password_hash(userPassword))
        if User.check_user_exists(email):
            return jsonify({'status': 400,
                            'error': 'Admin account already exists'}), 400
    else:
        return jsonify({'error': 'invalid user'}), 400
    user_db.append(user.to_json())
    return jsonify({'status': 201, 'data': user.to_json(),
                    'message': 'Your Account was created successfuly'}), 201


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
                        'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'}), 400
    for search_data in user_db:
        if search_data['email'] == login_email and \
             check_password_hash(search_data['userpassword'], login_password):
            access_token = create_access_token(identity=search_data['email'])
            return jsonify({'status': 200, 'access_token': access_token,
                            'message': 'You are now loggedin'}), 200
    return jsonify({'status': 403, 'error': 'Wrong email or password'}), 403
