#!/usr/bin/env python3
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes the input password with salt using bcrypt.hashpw

    Args:
        password (str): The password to hash

    Returns:
        bytes: The salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
