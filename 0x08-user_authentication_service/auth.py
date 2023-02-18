#!/usr/bin/env python3
"""
_hash_password returns bytes hashed with bcrypt.hashpw
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import exists
import uuid


def _hash_password(password: str) -> str:
    """function to hash the password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """ uuid generator
    Returns:
        str: random uuid
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

    def create_session(self, email:str) -> str:
        """
        craete session
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

