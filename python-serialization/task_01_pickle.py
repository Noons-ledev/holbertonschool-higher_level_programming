#!/usr/bin/python3
"""
Module documentation
"""
import pickle
"""
serializing with that module this time
"""


class CustomObject:
    """
    Class documentation
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = bool(is_student)

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        method doc
        """
        with open(filename, 'wb') as file:
            tosavedata = pickle.dumps(self)
            file.write(tosavedata)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return (pickle.loads(file.read()))
        except Exception:
            return None