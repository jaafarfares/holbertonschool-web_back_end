#!/usr/bin/env python3
"""
BasicAuth class
"""
from models.user import User
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Tuple


class BasicAuth(Auth):
    """
    empty class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extract base64 here
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        function to decode base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            code = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(code)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        function to extract user credentails
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":")
        return email, password

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        user object from credentails
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for i in users:
            if i.is_valid_password(user_pwd):
                return i
        return None
