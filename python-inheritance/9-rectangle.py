#!/usr/bin/python3
"""
This module implements the Rectangle class that
inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Here we import the BaseGeometry module to use it's attributes
"""


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        This method initializes an instance from a class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str representation
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """
        returns area
        """
        return (self.__width * self.__height)
