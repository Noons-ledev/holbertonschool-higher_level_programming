#!/usr/bin/python3
"""
This module is for additionning two numbers
either float or int
if not, raises an error
"""


def add_integer(a, b=98):
    """
    Adds two values
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
