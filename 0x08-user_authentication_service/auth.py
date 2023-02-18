#!/usr/bin/env python3
"""
_hash_password returns bytes hashed with bcrypt.hashpw
"""
import bcrypt


def _hash_password(password):
    """function to hash the password"""
    if password:
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed
