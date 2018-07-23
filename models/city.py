#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import Relationship


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    state_id = Column(String(128), nullable=False)
    name = Column(String(60), nullable=False, ForeignKey("states.id"))
    places = Relationship("Place", backref="cities", cascade="delete")
