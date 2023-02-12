#!/usr/bin/python3
""" defines a class Mylist that inherits 'list'"""


class MyList(list):
    """ inherits the list base class and implements
        sorted print
    """

    def print_sorted(self):
        """ prints list sorted in ascending order """
        print(sorted(self))
