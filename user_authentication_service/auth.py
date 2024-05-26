#!/usr/bin/env python3
"""Auth"""
import bcrypt
from db import DB
import uuid
from user import User
# Handle SQLAlchemy version compatibility
try:
    from sqlalchemy.orm.exc import NoResultFound
except ImportError:
    from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Returns bytes in a salty hash of input PW"""
    hashed_password = bcrypt.hashpw(password.encode(
        'utf-8'), bcrypt.gensalt())
    return hashed_password


def _generate_uuid() -> str:
    """Generate new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists!")
        except NoResultFound:
            pass

        """If new, hash dat PW!"""
        hashed_password = _hash_password(password)
        """Save into DB"""
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Checking if uer is valid w/ bcrypt"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            """If user doesn't exist return False"""
            return False

        if user is None:
            """If user is None return False"""
            return False

        """Extract the hashed PW from user obj"""
        hashed_password = user.hashed_password

        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            """If PW matches, return true"""
            return True
        else:
            """If PW doesn't match return false"""
            return False

    def create_session(self, email: str) -> str:
        """Creates sesh ID"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        if user is None:
            return None

        session_id = str(uuid.uuid4())
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """It takes a single session_id string argument and
        returns the corresponding User or None."""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys user session by setting session ID to None"""
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """FInd user by token, if user doesn't exist raise ValueError"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError()

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update users PW with reset token"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid or expired reset token")

        hashed_password = _hash_password(password)
        self._db.update_user(
            user.id, hashed_password=hashed_password)
