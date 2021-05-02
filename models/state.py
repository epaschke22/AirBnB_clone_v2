#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete,delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """ getter for filestorage relationship cities states"""
        from models import storage
        city_list = []
        for key, obj in storage.all(City).items():
            if obj.state_id == self.id:
                city_list.append(obj)
        return city_list
