import json
import unittest

from app.api.pgp_utils import decrypt
from tests.helpers import make_json_payload


class PGPDecryptTest(unittest.TestCase):

    def setUp(self):
        self.plain_text = 'This is only a test message. Please disregard.'
        self.passphrase = 'topsecret'
        payload = make_json_payload(
            message=self.plain_text,
            passphrase=self.passphrase
        )
        self.encrypted_message = json.loads(payload)['message']

    def test_decrypt_function_returns_correct_message(self):
        result = decrypt(
            encrypted_message=self.encrypted_message,
            passphrase=self.passphrase
        )
        self.assertEqual(result, self.plain_text)
