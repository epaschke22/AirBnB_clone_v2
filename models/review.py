#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = Column(String(1024), nullable=False)
