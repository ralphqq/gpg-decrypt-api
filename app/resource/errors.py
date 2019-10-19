from flask_restful import abort


def abort_bad_input_params(payload, params):
    """Checks if payload has required input params and is of valid type.

    Args:
        payload (dict): the payload to be evaluated
        params (iterable): a sequence of the required keys
    """
    if not isinstance(payload, dict):
        abort(400, message='Not a valid JSON format.')

    for param in params:
        if param not in payload:
            abort(400, message=f'{param} parameter not found.')

def abort_no_payload():
    """Called when no JSON payload is passed with the request."""
    abort(400, message='No payload passed.')

def abort_failed_decryption():
    """Called when input has invalid format or has invalid passphrase."""
    abort(400, message='Invalid GPG format or invalid passphrase')
