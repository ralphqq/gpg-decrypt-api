import pgpy


def decrypt(encrypted_message, passphrase):
    """Decrypts a PGP-encrypted message with given passphrase.

    Returns:
        str: the decrypted message
    """
    try:
        msg = pgpy.PGPMessage.from_blob(encrypted_message)
        decrypted_msg = msg.decrypt(passphrase)
        return decrypted_msg.message
    except Exception as e:
        raise e
