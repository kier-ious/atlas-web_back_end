#!/usr/bin/env python3
"""Child class of Auth"""
import base64
from typing import Tuple
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a base64 str"""
        if base64_authorization_header is None or \
            not isinstance(base64_authorization_header, str) or \
                not base64_authorization_header:
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            """Convert decoded bytes to utf-8 str"""
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception as e:
            """Hnadle the decoding errors"""
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Returns the user email and pw from the Base64 decoded value"""
        if decoded_base64_authorization_header is None or \
            not isinstance(decoded_base64_authorization_header, str) or \
                ':' not in decoded_base64_authorization_header:
            return None, None

        user_credintials = decoded_base64_authorization_header.split(':', 1)
        return user_credintials[0], user_credintials[1]
