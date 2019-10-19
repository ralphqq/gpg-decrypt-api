import json

from flask import request
from flask_restful import Resource

from app.common.gpg_utils import decrypt, DecryptionError
from app.resource.errors import (
    abort_bad_input_params,
    abort_failed_decryption,
    abort_no_payload
)


class DecryptMessage(Resource):

    def post(self):
        payload = request.get_json()
        if payload is None:
            abort_no_payload()
        abort_bad_input_params(payload, params=['message', 'passphrase'])

        try:
            result = decrypt(
                encrypted_message=payload['message'],
                passphrase=payload['passphrase']
            )
            return {'DecryptedMessage': result}
        except DecryptionError:
            abort_failed_decryption()
