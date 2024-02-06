#!/usr/bin/env python3
""" Authentication Module """

from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from typing import Union
from user import User
from db import DB


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


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:

        """ Registers User"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

        else:
            raise ValueError(f"User {email} already exists")