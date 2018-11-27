import uuid
import datetime


incident_db = []


class Incident:
    def __init__(self, createdBy, type, location,
                 Images, Videos, comment):
        self.incident_id = uuid.uuid4()
        self.createdOn = datetime.datetime.now()
        self.createdBy = createdBy
        self.type = type
        self.location = location
        self.Images = Images
        self.Videos = Videos
        self.comment = comment
        self.status = 'Draft'

    def to_json(self):
        return {
                 "incident_id": str(self.incident_id.int)[:10],
                 "createdOn": self.createdOn,
                 "createdBy": self.createdBy,
                 "type": self.type,
                 "location": self.location,
                 "Images": self.Images,
                 "Videos": self.Videos,
                 "comment": self.comment,
                 "status": self.status
               }

    @staticmethod
    def check_incident_record(id):
        for incident in incident_db:
            if incident['incident_id'] == id:
                return incident
