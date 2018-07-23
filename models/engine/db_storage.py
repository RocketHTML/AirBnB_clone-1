#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
from sqlalchemy import create_engine, MetaData
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
import models

class DBStorage:
	__engine = None
	__session = None

	def __init__(self):
        """
        Initialization Method
        """
        user = os.getenv('HBNB_MYSQL_USER', default=None)
        pw = os.getenv('HBNB_MYSQL_PWD', default=None)
        host = os.getenv('HBNB_MYSQL_HOST', default=None)
        db = os.getenv('HBNB_MYSQL_DB', default=None)
        form = "mysql+mysqldb://{}:{}@{}/{}"
        connection = form.format(user, pw, host, db)
        self.__engine = create_engine(connection, pool_pre_ping=True)

	def all(self, cls=None):
        """
        query current database based on cls name
        """
		pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass