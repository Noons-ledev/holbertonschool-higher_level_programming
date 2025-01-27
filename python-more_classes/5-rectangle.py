#!/usr/bin/python3
"""
This module is used to define the rectangle class and
attributes and methods we'll find with it
"""


class Rectangle:
    """
    Here we'll implement some methods and attributes
    """
    def __init__(self, width=0, height=0):
        """
        initializes an instance of the class
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        str representation of the object
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return (("#" * self.width + "\n") * self.height).strip()

    def __repr__(self):
        """
        representation of the instance
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        this method handles how
        an instance will be deleted
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Returns width of an instance
        """
        return self.__width

    @property
    def height(self):
        """
        Returns height of an instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method used to set height on another value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        This method returns area of the instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This method will get the
        rectangle perimeter and return it
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
