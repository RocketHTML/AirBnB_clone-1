#!/usr/bin/python3
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
		self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

	def all(self, cls=None):
		pass

	def new(self, obj):
		pass

	def save(self):
		pass

	def delete(self, obj=None):
		pass

	def reload(self):
		pass