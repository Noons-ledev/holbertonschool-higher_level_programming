#!/usr/bin/python3
"""
This module implements the is kind of class function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class
    of if it inherits from a parent class
    """
    return (isinstance(obj, a_class))
