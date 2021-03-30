#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.review import Review
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    reviews = relationship("Review", cascade="all,delete,delete-orphan",
                           backref="place")

    @property
    def reviews(self):
        """ getter for filestorage relationship cities states"""
        review_list = {}
        for key, obj in storage.all(Review):
            if obj.state_id == self.id:
                review_list[key] = obj
        return review_list
