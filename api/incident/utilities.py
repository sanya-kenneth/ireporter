import re


class validateIncident:
    def __init__(self, createdBy, type, location,
                 Images, Videos, comment):
        self.createdBy = createdBy
        self.type = type
        self.location = location
        self.Images = Images
        self.Videos = Videos
        self.comment = comment

    def validate_createdBy(self):
        return isinstance(self.createdBy, str) and \
         not re.search(r'[\s]', self.createdBy)

    def validate_type(self):
        return isinstance(self.type, str) and self.type == 'red-flag' \
         or self.type == 'intervention'

    def validate_location(self):
        return isinstance(self.location, int)

    def validate_comment(self):
        return isinstance(self.comment, str)
