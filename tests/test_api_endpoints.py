import json

from tests.base_setup import BaseTestCase


class DecryptMessageEndpointTest(BaseTestCase):

    def test_valid_post_request_returns_okay(self):
        response = self.send_request(
            url='/',
            method='post',
            data=json.dumps({
                'message': 'X',
                'passphrase': 'Y'
            })
        )

        self.assertEqual(response.status_code, 200)

    def test_get_request_returns_405_status(self):
        response = self.send_request(
            url='/',
            method='get',
            data=json.dumps({
                'message': 'X',
                'passphrase': 'Y'
            })
        )
        self.assertEqual(response.status_code, 405)
