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

    def print_sorted(self):
        """
        prints the sorted version of the object
        """
        print(sorted(self))
