import uuid
import datetime


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

    def to_json(self):
        return {
                 "incident_id": str(self.incident_id.int)[:10],
                 "createdOn": self.createdOn,
                 "createdBy": self.createdBy,
                 "type": self.type,
                 "location": self.location,
                 "Images": self.Images,
                 "Videos": self.Videos,
                 "comment": self.comment
               }
