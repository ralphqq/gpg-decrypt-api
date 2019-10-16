from flask import jsonify, request

from app.api import bp


@bp.route('/', methods=['POST'])
def decrypt_message():
    payload = data = request.get_json()
    return jsonify(
        {
            'message': 'Decrypted message',
            'passphrase': 'passphrase'
        }
    )
