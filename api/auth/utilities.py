import re


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
