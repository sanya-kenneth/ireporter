from flask import request, jsonify, json
from api.auth import auths
from api.auth.models import User, Admin
from api.auth.utilities import validateUser
from validate_email import validate_email
from werkzeug.security import generate_password_hash, check_password_hash


user_db = []

@auths.route('/users', methods=['POST'])
def signup():
   data = json.loads(request.data)
   firstName = data['firstname']
   lastName = data['lastname']
   otherNames = data['othernames']
   email = data['email']
   phoneNumber = data['phonenumber']
   userName = data['username']
   userPassword = data['password']
   if not firstName or not lastName or not\
           otherNames or not email or not phoneNumber or not \
           userName or not userPassword:
      return jsonify({'status': 400,
                     'error': 'Required field cannot be empty'}), 400
   if not validateUser.validate_names(firstName) or not \
           validateUser.validate_names(lastName) or not \
           validateUser.validate_names(otherNames) or not \
           validateUser.validate_names(userName):
      return jsonify({'status': 400,
                     'error': 'Name must be a string and must not contain spaces'}), 400
   if not validateUser.validate_phoneNumber(phoneNumber):
      return jsonify({'status': 400,
                      'error': 'Only numbers are allowed for the phonenumber field'}), 400
   if not validate_email(email):
      return jsonify({'status': 400, 'error': 'Invalid email'}), 400
   if not validateUser.validate_password(userPassword):
      return jsonify({'status': 400,
                      'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'}), 400
   for user in user_db:
      if user['email'] == email:
         return jsonify({'status': 400,
                         'error': 'User account already exists'}), 400
   user = User(firstName, lastName, otherNames, email,
               phoneNumber, userName, generate_password_hash(userPassword))
   user_db.append(user.to_json())
   return jsonify({'status': 201, 'data': user.to_json(),
                   'message': 'Your Account was created successfuly'}), 201


@auths.route('/users/admin', methods=['POST'])
def admin_signup():
   admin_data = json.loads(request.data)
   admin_firstname = admin_data['firstname']
   admin_lastname = admin_data['lastname']
   admin_othernames = admin_data['othernames']
   admin_email = admin_data['email']
   admin_phonenumber = admin_data['phonenumber']
   admin_username = admin_data['username']
   admin_password = admin_data['password']
   if not admin_firstname or not admin_lastname or not\
           admin_othernames or not admin_email or not\
           admin_phonenumber or not admin_username or not\
           admin_password:
      return jsonify({'status': 400,
                     'error': 'Required field cannot be empty'}), 400
   if not validateUser.validate_names(admin_firstname) or not \
           validateUser.validate_names(admin_lastname) or not \
           validateUser.validate_names(admin_othernames) or not \
           validateUser.validate_names(admin_username):
      return jsonify({'status': 400,
                     'error': 'Name must be a string and must not contain spaces'}), 400
   if not validateUser.validate_phoneNumber(admin_phonenumber):
      return jsonify({'status': 400,
                      'error': 'Only numbers are allowed for the phonenumber field'}), 400
   if not validate_email(admin_email):
      return jsonify({'status': 400, 'error': 'Invalid email'}), 400
   if not validateUser.validate_password(admin_password):
      return jsonify({'status': 400,
                      'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'}), 400
   for admin in user_db:
      if admin['email'] == admin_email:
         return jsonify({'status': 400,
                         'error': 'Admin account already exists'}), 400
   admin = Admin(admin_firstname, admin_lastname, admin_othernames,
                 admin_email, admin_phonenumber, admin_username, admin_password)
   user_db.append(admin.to_json())
   return jsonify({'status': 201, 'data': admin.to_json(),
                   'message': 'Your Account was created successfuly'}), 201


@auths.route('/users/login', methods=['POST'])
def login():
   login_info = json.loads(request.data)
   login_email = login_info['email']
   login_password = login_info['password']
   if not login_email or not login_password:
      return jsonify({'status': 400,
                      'error': 'email or password cannot be empty'}), 400
   if not validate_email(login_email):
      return jsonify({'status': 400, 'error': 'Invalid email'}), 400
   if not validateUser.validate_password(login_password):
      return jsonify({'status': 400,
                      'error': 'Password must be atleast 8 characters and should have atleast one number and one capital letter'}), 400
   for search_data in user_db:
      print(search_data)
      if search_data['email'] == login_email and \
          check_password_hash(search_data['userpassword'], login_password):
         return jsonify({'status': 200, 'message': 'You are now loggedin'}), 200
   return jsonify({'satus': 401, 'error':'Wrong email or password'}), 401
