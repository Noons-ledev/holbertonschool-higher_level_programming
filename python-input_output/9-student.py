#!/usr/bin/python3
"""
Module documentation
"""


class Student:
    """
    Class documentation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes an instance of a class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Doc here
        """
        return vars(self)
