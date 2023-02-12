#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """ returns a list of available attributes and methods of the object
        param: obj(object) - object to get attributes and methods from
    """
    return dir(obj)
