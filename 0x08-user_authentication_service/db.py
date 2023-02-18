#!/usr/bin/env python3
"""DB module
"""
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
        self._engine = create_engine("sqlite:///a.db", echo=False)
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
        """
        add user a to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **id) -> User:
        """ function to find the user
        query the first user from database table
        """
        if not id:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**id).first()
        if not user:
            raise NoResultFound

    def update_user(self, user_id: int, **args) -> None:
        """user update method"""
        if not user_id:
            raise ValueError
        try:
            self._session.query(User).filter(
                self.find_user_by(id=user_id)).update(args)
        except ValueError:
            raise ValueError
        self._session.commit()
