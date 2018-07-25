#!/usr/bin/python3
'''
    Testing the db_storage module.
'''

import os
import setenv
import unittest
import utility



class testDBStorage(unittest.TestCase):
    '''
        Testing the DBStorage class
    '''

    def setUp(self):
        '''
            Initializing tables and declaritive classes, and open session

            Set storage to FileStorage when host machine doesn't have mysql installed
        '''
        utility.env_switcher('file')
        from models.base_model import BaseModel
        from models.engine.db_storage import DBStorage
        from models.engine.file_storage import FileStorage
        
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.storage = DBStorage()
        else:
            self.storage = FileStorage()
        self.storage.reload()
        ## insert some starter data - after testing insert capability

    def test_empty(self):
        '''
            Empty test to ensure there are no errors
        '''
        self.assertEqual(True, True)