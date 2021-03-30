#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref="parent"
    )

    @property
    def cities(self):
        """ getter for filestorage relationship cities states"""
        city_list = {}
        for key, obj in storage.all(City):
            if obj.state_id == self.id:
                city_list[key] = obj
        return city_list
