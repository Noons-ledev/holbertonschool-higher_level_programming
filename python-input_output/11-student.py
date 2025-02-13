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

    def to_json(self, attrs=None):
        """
        Doc here
        """
        if attrs is None:
            return vars(self)
        else:
            mydict = {}
            for i in attrs:
                if hasattr(self, i):
                    mydict[i] = getattr(self, i)
        return mydict

    def reload_from_json(self, json):
        """
        doc here
        """
        for key in json:
            setattr(self, key, json[key])

