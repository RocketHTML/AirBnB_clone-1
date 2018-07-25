#!/usr/bin/python3
'''
    Testing the db_storage module.
'''

import os
import setenv
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


class testDBStorage(unittest.TestCase):
    '''
        Testing the DBStorage class
    '''

    def setUp(self):
        '''
            Initializing tables and declaritive classes, and open session
        '''
        self.storage = DBStorage()
        self.storage.reload()
        ## insert some starter data - after testing insert capability

    def test_empty(self):
        '''
            Empty test to ensure there are no errors
        '''
        assertEqual(True, True)