#!/usr/bin/python3
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
        
