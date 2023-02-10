#!/usr/bin/env python3
"""
SessionAuth class
"""
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """1. Empty session
    Args:
        Auth (_class_): inherits from class Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """_summary_
        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = int(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_summary_
        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
