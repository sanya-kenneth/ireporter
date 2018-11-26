import uuid
import datetime


class User:
    def __init__(self, firstname, lastname, othernames,
                 email, phoneNumber, username, password):
        self.user_id = uuid.uuid4()
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
        return {
                 "user_id": str(self.user_id.int)[:10],
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


class Admin(User):
    def __init__(self, *args, **kwargs):
        User.__init__(self, *args, **kwargs)
        self.isAdmin = True
