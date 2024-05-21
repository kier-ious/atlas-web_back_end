#!/usr/bin/env python3
"""Child class of Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Child class inheriting from parent, currently empty"""
    pass

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Returns the Base64 part of Auth header for BasicAuth"""
        if authorization_header is None or \
            not isinstance(authorization_header, str) or \
            not authorization_header.startswith('Basic '):
                return None

        return authorization_header.split(' ')[1]
