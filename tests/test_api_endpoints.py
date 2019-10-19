import json
from unittest.mock import patch

from app.common.gpg_utils import DecryptionError
from tests.base_setup import BaseTestCase
from tests.helpers import make_json_payload

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
            data=make_json_payload(
                message=self.plain_text,
                passphrase=self.passphrase
            )
        )

        # To ensure patch gets cleaned up during tearDown:
        self.addCleanup(patcher.stop)

    def test_valid_post_request_calls_decrypt_and_returns_okay(self):
        self.assertTrue(self.mock_decrypt.called)
        self.assertEqual(self.response.status_code, 200)

    def test_get_request_returns_405_status(self):
        self.mock_decrypt.called = False # Should still be False after below
        response = self.send_request(
            url='/decryptMessage',
            method='get',
            data=json.dumps({
                'message': 'X',
                'passphrase': 'Y'
            })
        )
        self.assertFalse(self.mock_decrypt.called)
        self.assertEqual(response.status_code, 405)

    def test_response_has_correct_format(self):
        self.assertEqual(self.response.content_type, 'application/json')
        self.assertIsInstance(self.response.get_json(), dict)

    def test_response_payload_has_correct_fields(self):
        payload = self.response.get_json()
        for field in PAYLOAD_FIELDS:
            self.assertIn(field, payload)

    def testno_payload_error(self):
        self.mock_decrypt.called = False
        response = self.send_request(url='/decryptMessage', method='post')
        self.assertFalse(self.mock_decrypt.called)
        self.assertEqual(response.status_code, 400)

    def test_missing_message_param(self):
        self.mock_decrypt.called = False
        response = self.send_request(
            url='/decryptMessage',
            method='post',
            data=json.dumps({'passphrase': 'passphrase'})
        )
        self.assertFalse(self.mock_decrypt.called)
        self.assertEqual(response.status_code, 400)

    def test_missing_passphrase_param(self):
        self.mock_decrypt.called = False
        response = self.send_request(
            url='/decryptMessage',
            method='post',
            data=json.dumps({'message': 'message'})
        )
        self.assertFalse(self.mock_decrypt.called)
        self.assertEqual(response.status_code, 400)

    def test_decryption_errors_return_status_400(self):
        self.mock_decrypt.called = False    # This will be True later
        self.mock_decrypt.side_effect = DecryptionError
        response = self.send_request(
            url='/decryptMessage',
            method='post',
            data=json.dumps({
                'message': self.plain_text,
                'passphrase': self.passphrase
            })
        )
        self.assertTrue(self.mock_decrypt.called)
        self.assertEqual(response.status_code, 400)
