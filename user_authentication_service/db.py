#!/usr/bin/env python3
"""DataBase"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
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

    def find_user_by(self, **kwargs) -> User:
        """Finds user with kwargs

        Returns:
            User: User that fits requirements
        """
        try:
            user = self.__session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("No user fits requirements.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments provided.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates user attributes

        Args:
            user_id (int): ID for user
            **kwargs: Random keyword for updating user info
        """
        try:
            """Locate user by their ID"""
            user = self.find_user_id(id=user_id)

            """Update their info"""
            for attr, value in kwargs.items():
                if hasattr(user, attr):
                    setattr(user, attr, value)
                else:
                    raise ValueError(f"Invalid argument: {attr}")

            """Commit changes to DB"""
            self._session.commit()
        except NoResultFound:
            raise NoResultFound(f"No user found with user_id: {user_id}")
        except InvalidRequestError as e:
            raise InvalidRequestError(
                "Invalid query arguments provided") from e
