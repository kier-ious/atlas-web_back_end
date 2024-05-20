#!/usr/bin/env python3
"""Creating a class to manage the API auth"""

from flask import request
from typing import List, TypeVar


class Auth():
    """This class is the template for
    all authentication system you will implement."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """eturns False - path and excluded_paths will be used
        later, now, you don’t need to take care of them"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns none-request will be flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None-request will be the flask request object"""
        return None
