#!/usr/bin/python3
"""
This module defines a class
"""


class Square:

    """
    Here is my Square class
    we'll add attributes here later
    """

    def __init__(self, size=0):
        """
        This method initializes the square with
        a private instance attribute (size)
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This method will return the area of a square
        """
        self.aera = self.__size * self.__size
        return self.aera

    @property
    def size(self):
        """
        This method will allow to retrieve
        size of the square,
        which is a private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method will be used
        to set a new value to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
