import datetime


incident_db = []


class Incident:
    """model class for an incident record """
    def __init__(self, createdBy, record_type, location,
                 Images, Videos, comment):
        self.incident_id = len(incident_db)+1
        self.createdOn = datetime.datetime.now()
        self.createdBy = createdBy
        self.record_type = record_type
        self.location = location
        self.Images = Images
        self.Videos = Videos
        self.comment = comment
        self.status = 'Draft'

    def to_json(self):
        """method converts data from the incident class object to json format"""
        return {
                 "incident_id": self.incident_id,
                 "createdOn": self.createdOn,
                 "createdBy": self.createdBy,
                 "incident_type": self.record_type,
                 "location": self.location,
                 "Images": self.Images,
                 "Videos": self.Videos,
                 "comment": self.comment,
                 "status": self.status
               }
