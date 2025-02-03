#!/usr/bin/python3
"""
This module implements the basegeometry class
"""


class BaseGeometry:
    """
    This class is empty for now
    """
    def __init__(self):
        """
        Does nothing for now
        """
        pass

    def area(self):
        """
        Raises an error for now due to lack of implementation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method will validate value if conditions are respected
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
