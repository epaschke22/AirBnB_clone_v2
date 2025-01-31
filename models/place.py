#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = relationship("Amenity", secondary=place_amenity,
                               viewonly=False)
    reviews = relationship("Review", cascade="all,delete,delete-orphan",
                           backref="place")

    @property
    def reviews(self):
        """ getter for filestorage relationship cities states"""
        from models import storage
        review_list = {}
        for key, obj in storage.all(Review):
            if obj.place_id == self.id:
                review_list[key] = obj
        return review_list

    @property
    def amenities(self):
        """amenities getter"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """amenities setter"""
        from models.amenity import Amenity
        if obj is type(Amenity):
            self.amenity_ids.append(obj.id)
