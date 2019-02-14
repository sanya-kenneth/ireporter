import datetime


class User:
    """model class for users.
    By default isAdminis set to false when a user object is created """
    def __init__(self, firstname, lastname, othernames,
                 email, phoneNumber, username, password, isAdmin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password
        self.registered = datetime.datetime.now()
        self.isAdmin = isAdmin
