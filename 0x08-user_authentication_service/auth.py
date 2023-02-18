#!/usr/bin/env python3
"""
_hash_password returns bytes hashed with bcrypt.hashpw
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """function to hash the password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
