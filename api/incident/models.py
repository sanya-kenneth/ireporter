import datetime


class Incident:
    """model class for an incident record """
    def __init__(self, createdBy, record_type, location,
                 Images, comment):
        self.createdOn = datetime.datetime.now()
        self.createdBy = createdBy
        self.record_type = record_type
        self.location = location
        self.Images = Images
        self.comment = comment
        self.status = 'Draft'
