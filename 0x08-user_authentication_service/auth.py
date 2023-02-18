#!/usr/bin/env python3
"""
_hash_password returns bytes hashed with bcrypt.hashpw
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import exists
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """function to hash the password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def _generate_uuid () -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return str(uuid.uuid4())
        

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        validate the user Credentials
        """
        try:
            self._db.find_user_by(email=email)
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            if bcrypt.checkpw(password.encode('utf-8'), hashed):
                return True
        except (ValueError, AttributeError,  NoResultFound):
            return False

