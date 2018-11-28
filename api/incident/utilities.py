import re


class validateIncident:
    @staticmethod
    def validate_type(record_type):
        return isinstance(record_type, str) and record_type == 'red-flag' \
         or record_type == 'intervention'

    @staticmethod
    def validate_comment(comment):
        return isinstance(comment, str)

    @staticmethod
    def validate_status(status):
        return isinstance(status, str) and status == \
            'under investigation' or status == 'rejected' or \
            status == 'resolved'

    @staticmethod
    def validate_images_and_video(image_or_video):
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
        value1 = float(location[0])
        value2 = float(location[1])
        return isinstance(location, list) and isinstance(value1, float) and\
         isinstance(value2, float) and len(location) == 2
