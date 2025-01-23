#!/usr/bin/python3
"""
This module helps printing
both fist and last name passed as argument
to the function
"""


def say_my_name(first_name, last_name=""):
    """
    Checks first for string only as arguments
    if not, raises errors
    then performs the print
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
