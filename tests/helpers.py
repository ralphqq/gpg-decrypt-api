import json

import gnupg


def make_json_payload(message, passphrase):
    """Creates JSON payload to be sent to API endpoint.

    Args:
        - message (str): the text to be encrypted
        passphrase (str): passphrase to be used in the encryption

    Returns:
        JSON object that contains the following key-value pairs:
            'message': the GPG-encrypted text
            'passphrase': passphrase used to encrypt
    """
    gpg = gnupg.GPG()
    msg = gpg.encrypt(
        data=message,
        passphrase=passphrase,
        recipients=None,
        symmetric='AES256'
    )
    return json.dumps({
        'message': str(msg),
        'passphrase': passphrase
    })
