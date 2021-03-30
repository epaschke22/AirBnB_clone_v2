#!/usr/bin/python3
"""This module defines a mysql database for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """This class manages a mysql database with sqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                       HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV is 'test':
            __session().delete().all()

    def all(self, cls=None):
        """calls a query on the whole database"""
        if cls is None:
            query = __session().query().all()
        else:
            query = __session(cls).query().all()
        output = {}
        for item in query:
            output[type(item).__name__] = item
        return output

    def new(self, obj):
        """adds object to current database"""
        __session.add(obj)

    def save(self):
        """commits all changes to current database"""
        __session.commit()

    def delete(self, obj=None):
        """deletes obj from current database"""
        if obj is not None:
            __session.delete(obj)

    def reload(self):
        """creates tables and session from current database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        __session = scoped_session(session_factory)
