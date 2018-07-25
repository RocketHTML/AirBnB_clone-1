#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
import utility
#from models.base_model import BaseModel
#from models.city import City

BaseModel = ''
City = ''

class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def setUp(self):
        ''' appropriately set the environment for testing '''

        utility.env_switcher('file')
        base_model = __import__('models.base_model')
        city = __import__('models.city')
        utility.reload_modules([base_model, city])
        global BaseModel
        global City
        BaseModel = base_model.BaseModel
        City = city.City

    def test_City_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)
