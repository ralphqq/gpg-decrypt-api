import json
import unittest

from app import create_app


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(app_settings='config.TestingConfig')
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def send_request(self, url='/', method='get', data=None):
        """Helper method to send an HTTP request and get a response.

        Args:
            url (str): the URL associated with the view to be called
            method (str): the HTTP request method; can either be 
                'get' or 'post'
            data (object): data to be passed in as part of request
        """
        response = None
        if method.lower() == 'get':
            response = self.client.get(
                url,
                data=json.dumps(data),
                content_type='application/json'
            )
        elif method.lower() == 'post':
            response = self.client.post(
                url,
                data=json.dumps(data),
                content_type='application/json'
            )

        return response
