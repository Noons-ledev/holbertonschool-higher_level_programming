#!/usr/bin/python3
"""
This module defines a class
and the methods that can be used by its attributes
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
        self.size = size
        if not isinstance(position, tuple) or\
            not all(isinstance(value, int) for value in position)\
                or not all(value >= 0 for value in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = position

    def area(self):
        """
        This method will return the area of a square
        """
        return self.__size ** 2

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        This method is used to set
        square's position on another value
        """
        if not isinstance(value, tuple) or len(value) != 2\
            or not all(isinstance(element, int) for element in value)\
                or not all(element >= 0 for element in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        This method will print a square of #
        depending on its size
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
