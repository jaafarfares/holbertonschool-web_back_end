#!/usr/bin/env python3
"""
SessionAuth class
"""
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from typing import List, TypeVar
import base64




@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
