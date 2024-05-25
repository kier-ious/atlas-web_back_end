#!/usr/bin/env python3
"""SQLAlchemy model named User for a database table"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """SQLAlchemy model named User for a database table"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
