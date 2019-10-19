import json
import unittest

from app.common.gpg_utils import decrypt, DecryptionError
from tests.helpers import make_payload


class PGPDecryptTest(unittest.TestCase):

    def setUp(self):
        self.plain_text = 'This is only a test message. Please disregard.'
        self.passphrase = 'topsecret'
        payload = make_payload(
            message=self.plain_text,
            passphrase=self.passphrase
        )
        self.encrypted_message = payload['message']

    def test_decrypt_function_returns_correct_message(self):
        result = decrypt(
            encrypted_message=self.encrypted_message,
            passphrase=self.passphrase
        )
        self.assertEqual(result, self.plain_text)

    def test_incorrect_passphrase_raises_error(self):
        with self.assertRaises(DecryptionError):
            result = decrypt(
                encrypted_message=self.encrypted_message,
                passphrase='wrongpassphrase'
            )
