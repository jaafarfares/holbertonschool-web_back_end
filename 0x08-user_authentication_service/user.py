#!/usr/bin/env python3
"""
 create a SQLAlchemy model named User for a database table named users
"""
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):
    """
    class User
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)

    hashed_password = Column(String)
    session_id = Column(String)
    reset_token = Column(String)

    def __init__(self):
        """
        function reper
        """

        return (
            self.id,
            self.email,
            self.hashed_password,
            self.session_id,
            self.reset_token)
