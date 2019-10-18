from flask_restful import abort


def abort_bad_input_params(payload, params):
    """Checks if payload contains required input params.

    Args:
        payload (dict): the payload to be evaluated
        params (iterable): an iterable of the required keys
    """
    for param in params:
        if param not in payload:
            abort(400, message=f'{param} is a required input parameter.')

def abort_no_payload():
    """Called when no JSON payload is passed with the request."""
    abort(400, message='No payload passed.')

def abort_failed_decryption():
    """Called when input has invalid format or has invalid passphrase."""
    abort(400, message='Invalid GPG format or invalid passphrase')
