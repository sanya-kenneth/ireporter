

class validateIncident:
    """validator class for incident records"""
    @staticmethod
    def validate_type(record_type):
        """method validates the type of incident record"""
        return isinstance(record_type, str) and record_type == 'red-flag' \
         or record_type == 'intervention'

    @staticmethod
    def validate_comment(comment):
        """method validates the comment being attached
        to an incident record"""
        return isinstance(comment, str)

    @staticmethod
    def validate_status(status):
        """method validates the status of an incident record"""
        return isinstance(status, str) and status == \
            'under investigation' or status == 'rejected' or \
            status == 'resolved'

    @staticmethod
    def validate_images_and_video(image_or_video):
        """method validates metadata of videos or images"""
        title_key = 'title'
        url_key = 'url'
        store_keys = []
        store_values = []
        for keys, values in image_or_video.items():
            store_keys.append(keys)
            store_values.append(values)
        return title_key in store_keys and url_key in store_keys and\
               isinstance(store_values[0], str) and \
               isinstance(store_values[1], str)

    @staticmethod
    def validate_location(location):
        """method validates the location of an incident record"""
        return isinstance(location, list) and len(location) == 2\
         and isinstance(location[0], float) and isinstance(location[1], float)
