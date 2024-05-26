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


def _hash_password(password: str) -> bytes:
    """Returns bytes in a salty hash of input PW"""
    _hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return _hash_password
