#!/usr/bin/env python3
"""
SessionAuth class
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """1. Empty session
    Args:
        Auth (_class_): inherits from class Auth
    """
    pass
