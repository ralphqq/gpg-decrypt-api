import gnupg


class DecryptionError(Exception):
    """Thrown when decryption fails."""
    pass


def decrypt(encrypted_message, passphrase):
    """Decrypts a GPG-encrypted message with given passphrase.

    Args:
        - encrypted_message (str): the GPG-encrypted text to be decrypted
        - passphrase (str): the passphrase to be used

    Returns:
        str: the decrypted message
    """
    try:
        gpg = gnupg.GPG()
        msg = gpg.decrypt(encrypted_message, passphrase=passphrase)
        if not msg.ok:
            raise ValueError('Unable to decrypt')
        return str(msg)
    except Exception as e:
        raise DecryptionError(e)
