#!/usr/bin/python3
''' This script sets up the environment for testing '''
import os

os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
os.environ['HBNB_MYSQL_HOST'] = 'localhost'
os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
os.environ['HBNB_ENV'] = 'test'
os.environ['HBNB_TYPE_STORAGE'] = 'db'