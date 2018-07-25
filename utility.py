#!/usr/bin/python3
''' This module holds utility functions used for testing '''
import os
import importlib

def dict_checker(answer_list, obj):
    ''' makes sure that obj contains all keys in answer_list 

        Return: the key that is missing, or None if all keys are present
    '''
    failures = []
    for answer in answer_list:
        if answer not in vars(obj):
            failures.append(answer)
    return failures

def env_switcher(mode):
    ''' switches the environment variables to the specified mode '''
    os.environ['HBNB_ENV'] = 'test'
    os.environ['HBNB_MYSQL_HOST'] = 'localhost'
    os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
    os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
    os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
    if mode == 'db':
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
    else:
        os.environ['HBNB_TYPE_STORAGE'] = 'file'

def reload_modules(modules):
    ''' reloads specified modules to account for environment changes '''
    for module in modules:
        importlib.reload(module)