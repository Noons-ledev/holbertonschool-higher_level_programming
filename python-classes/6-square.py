#!/usr/bin/python3
"""
This module defines a class
"""


class Square:

    """
    Here is my Square class
    we'll add attributes here later
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This method initializes the square with
        a private instance attribute (size) and position
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        This method retrieves the position of the square
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        This method is used to set
        square's position on another value
        """
        if not isinstance(value, tuple) or\
            not all(isinstance(element, int) for element in value)\
                or not all(element > 0 for element in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        This method will print a square of #
        depending on its size
        """
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
