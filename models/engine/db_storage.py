#!/usr/bin/python3
"""This module defines a mysql database for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
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
        usr = getenv('HBNB_MYSQL_USER')
        psw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (usr, psw, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') is 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """calls a query on the whole database"""
        classlist = [State, City, User, Place, Review, Amenity]
        output = {}
        if cls is None:
            for clsname in classlist:
                queryall = self.__session.query(clsname).all()
                for obj in queryall:
                    output["{}.{}".format(type(obj).__name__, obj.id)] = obj
        else:
            queryall = self.__session.query(cls).all()
            for obj in queryall:
                output["{}.{}".format(type(obj).__name__, obj.id)] = obj
        return output

    def new(self, obj):
        """adds object to current database"""
        self.__session.add(obj)

    def save(self):
        """commits all changes to current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from current database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates tables and session from current database"""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """calls close method to end session"""
        self.__session.close()
