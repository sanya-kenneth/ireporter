import datetime


user_db = []


class User:
    """model class for users.
    By default isAdminis set to false when a user object is created """
    def __init__(self, firstname, lastname, othernames,
                 email, phoneNumber, username, password):
        self.user_id = len(user_db)+1
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password
        self.registered = datetime.datetime.now()
        self.isAdmin = False

    def to_json(self):
        """method returns data from the user class instance as json data"""
        return {
                 "user_id": self.user_id,
                 "firstname": self.firstname,
                 "lastname": self.lastname,
                 "othername": self.othernames,
                 "email": self.email,
                 "phoneNumber": self.phoneNumber,
                 "username": self.username,
                 "userpassword": self.password,
                 "registered": self.registered,
                 "isAdmin": self.isAdmin
               }

    @staticmethod
    def check_user_exists(email):
        """method checks if a user exists in the system"""
        for user in user_db:
            return user['email'] == email


class Admin(User):
    """model class for an admin. when an instance of 
    this class is created, isAdmin is set to True """
    def __init__(self, fname, lname, admin_othernames,
                 admin_email, admin_mobile_number, admin_username, admin_password):
        self.user_id = len(user_db)+1
        self.firstname = fname
        self.lastname = lname
        self.othernames = admin_othernames
        self.email = admin_email
        self.phoneNumber = admin_mobile_number
        self.username = admin_username
        self.password = admin_password
        self.registered = datetime.datetime.now()
        self.isAdmin = True
