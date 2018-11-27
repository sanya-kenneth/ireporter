from api.incident.models import incident_db
from api.auth.models import user_db
from api import create_app
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        This method helps setup tests.
        It also initialises the test_client where tests will be run 
        """
        self.app = create_app('Testing')
        self.app = self.app.test_client()

    def tearDown(self):
        user_db.clear()
        incident_db.clear()


if __name__ == '__main__':
    unittest.main()
