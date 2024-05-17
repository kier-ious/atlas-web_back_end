#!/usr/bin/env python3
"""Implement a hash_password function that expects one
string argument name password and returns a salted, hashed password, which
is a byte string."""


import bcrypt


def hash_password(password: str) -> bytes:
    """Generates salt hash"""
    salt = bcrypt.gensalt()
    """Hash the password with salt"""
    """Hashbrowns"""
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates that the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
