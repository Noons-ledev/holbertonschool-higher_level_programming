#!/usr/bin/python3
"""
This module refers to the MyList class,
that inherits from list
"""


class MyList(list):
    """
    This class inherits from list and
    will implement methods to apply on
    """

    def __init__(self, list=[]):
        """
        initializes an instance of the class
        """
        super().__init__(list)

    def print_sorted(self):
        """
        prints the sorted version of the object
        """
        print(sorted(self))
