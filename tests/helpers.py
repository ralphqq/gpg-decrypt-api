import json

import pgpy


def make_json_payload(message, passphrase):
    """Creates JSON payload to be sent to API endpoint.

    Args:
        - message (str): the text to be encrypted
        passphrase (str): passphrase to be used in the encryption

    Returns:
        JSON object that contains the following key-value pairs:
            'message': the PGP-encrypted text
            'passphrase': passphrase used
    """
    msg = pgpy.PGPMessage.new(message)
    return json.dumps({
        'message': str(msg.encrypt(passphrase)),
        'passphrase': passphrase
    })
