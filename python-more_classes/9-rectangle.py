#!/usr/bin/python3
"""
This module is used to define the rectangle class and
attributes and methods we'll find with it
"""


class Rectangle:
    """
    Here we'll implement some methods and attributes
    """
    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def square(cls, size=0):
        """
        This method is used to create
        a rectangle with all datas from
        the same value
        and returns it
        """
        myrectangle = Rectangle(size, size)
        return myrectangle

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This static method will be used
        to compare two instances areas
        and returning the most area valued instance,
        or first instance in equality case
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def __init__(self, width=0, height=0):
        """
        initializes an instance of the class
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        str representation of the object
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return (("{}".format(self.print_symbol) * self.width + "\n")
                * self.height).strip()

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
        Rectangle.number_of_instances -= 1

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
