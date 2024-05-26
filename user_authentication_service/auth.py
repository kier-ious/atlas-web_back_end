#!/usr/bin/env python3
"""Auth"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
from db import DB


class Auth:
    """Auth class to interact with the authentication database."""
    def __init__(self):
        self._db = DB()

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """Returns bytes in a salty hash of input PW"""
        hashed_password = bcrypt.hashpw(password.encode(
            'utf-8'), bcrypt.gensalt())
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        existing_user = self._db.find_user_by(email=email)
        if existing_user:
            raise ValueError(f"User {email} already exists!")

        """If new, hash dat PW!"""
        hashed_password = self._hash_password(password)
        """Save into DB"""
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Checking if uer is valid w/ bcrypt"""
        user = self._db.find_user_by(email=email)
        if user:
            hashed_password = user.hashed_password
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        return False
