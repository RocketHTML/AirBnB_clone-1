#!/usr/bin/python3
<<<<<<< HEAD
'''
    Define class DatabaseStorage
'''
import sqlalchemy from Columns, String, create_engine
import os
import models


class DBStorage:
    '''
        Class Database Storage
    '''
    __engine = None
    __session = None

    def __init__(self):
    """
    Initialization Method
    """
    user = os.getenv('HBNB_MYSQL_USER', default=None)
    password = os.getenv('HBNB_MYSQL_PWD', default=None)
    host = os.getenv('HBNB_MYSQL_HOST', default=None)
    database_name = os.getenv('HBNB_MYSQL_DB', default=None)

    self.__engine = create_engine(connection.format(
        user, password, database_name), pool_pre_ping=True)
    if os.getenv('HBNB_ENV') == 'test':
        Base.metadata.drop_all(self.__enginge)

    def all(self, cls=None):
        """
        query current database based on cls name
        """
        
=======
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
	__engine = None
	__session = None

	def __init__(self):
		pass

	def all(self, cls=None):
		pass

	def new(self, obj):
		pass

	def delete(self, obj=None):
		pass

	def reload(self):
		pass
>>>>>>> 61cb8e9b75122780a9630c3db7912f0d653a035c
