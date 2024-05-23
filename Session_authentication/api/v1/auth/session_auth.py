#!/usr/bin/env python3
"""DOCDOCDOCDOC"""
import uuid
from api.v1.auth.auth import Auth


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
