#!/usr/bin/env python3
"""Child class of Auth"""
import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on his email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        """Begin user search in DB"""
        user = User.search({'email': user_email})
        if not user:
            return None

        user = user[0]

        """Checking PW is valid"""
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth and retrieves the User instance for a request"""
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_header = self.extract_base64_authorization_header(auth_header)
        if base64_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(base64_header)
        if decoded_header is None:
            return None

        email, password = self.extract_user_credentials(decoded_header)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
