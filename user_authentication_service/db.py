#!/usr/bin/env python3
"""DataBase"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds user to the DB

        Args:
            email (str): the users email
            hashed_password (str): the users PW

        Returns:
            User: info/object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        """Add user to session"""
        session = self._session
        
        session.add(new_user)

        session.commit()

        return new_user
