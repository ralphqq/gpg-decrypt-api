import json
from unittest.mock import patch

from app.common.gpg_utils import DecryptionError
from tests.base_setup import BaseTestCase
from tests.helpers import make_payload

PAYLOAD_FIELDS = ['DecryptedMessage']

class DecryptMessageEndpointTest(BaseTestCase):

    def setUp(self):
        # Patch the decrypt function
        patcher = patch(
            'app.resource.decrypt.decrypt',
            return_value='Decrypted message'
        )
        self.mock_decrypt = patcher.start()

        # Make a post request
        self.plain_text = 'X'
        self.passphrase = 'Y'
        self.response = self.send_request(
            url='/decryptMessage',
            method='post',
            data=make_payload(
                message=self.plain_text,
                passphrase=self.passphrase
            )
        )

        # To ensure patch gets cleaned up during tearDown:
        self.addCleanup(patcher.stop)

    def test_valid_post_request_calls_decrypt_and_returns_okay(self):
        self.assertTrue(self.mock_decrypt.called)
        self.assertEqual(self.response.status_code, 200)

    def test_response_has_correct_format(self):
        self.assertEqual(self.response.content_type, 'application/json')
        self.assertIsInstance(self.response.get_json(), dict)

    def test_response_payload_has_correct_fields(self):
        payload = self.response.get_json()
        for field in PAYLOAD_FIELDS:
            self.assertIn(field, payload)


@patch('app.resource.decrypt.decrypt', return_value='Decrypted message')
class DecryptMessageEndpointErrorsTest(BaseTestCase):

    def send_bad_request(self, method='post', data=None):
        """Helper method to send bad or invalid HTTP request."""
        return self.send_request(
            url='/decryptMessage',
            method=method,
            data=data
        )

    def test_get_request_returns_405_status(self, mock_decrypt):
        response = self.send_bad_request(method='get')
        self.assertFalse(mock_decrypt.called)
        self.assertEqual(response.status_code, 405)

    def testno_payload_error(self, mock_decrypt):
        response = self.send_bad_request()
        self.assertFalse(mock_decrypt.called)
        self.assertEqual(response.status_code, 400)

    def test_invalid_json_format_raises_bad_request(self, mock_decrypt):
        response = self.send_bad_request(data='invalid JSON format')
        self.assertFalse(mock_decrypt.called)
        self.assertEqual(response.status_code, 400)

    def test_missing_message_param(self, mock_decrypt):
        response = self.send_bad_request(data={'passphrase': 'passphrase'})
        self.assertFalse(mock_decrypt.called)
        self.assertEqual(response.status_code, 400)

    def test_missing_passphrase_param(self, mock_decrypt):
        response = self.send_bad_request(data={'message': 'message'})
        self.assertFalse(mock_decrypt.called)
        self.assertEqual(response.status_code, 400)

    def test_decryption_errors_return_status_400(self, mock_decrypt):
        mock_decrypt.side_effect = DecryptionError
        response = self.send_request(
            url='/decryptMessage',
            method='post',
            data={
                'message': 'x',
                'passphrase': 'y'
            }
        )
        self.assertTrue(mock_decrypt.called)
        self.assertEqual(response.status_code, 400)
