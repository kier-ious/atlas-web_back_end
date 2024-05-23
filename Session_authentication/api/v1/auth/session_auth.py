#!/usr/bin/env python3
"""DOCDOCDOCDOC"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """1st step to create authorization mechanism"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        """Generate a new Session ID"""
        session_id = str(uuid.uuid4())

        """Store session_id w/ same user_id"""
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on the Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        """Retrieves & return user ID for the session_id"""
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance baced on a cookie value"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    