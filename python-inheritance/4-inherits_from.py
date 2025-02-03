#!/usr/bin/python3
"""
This module implements the inherit from function
"""


def inherits_from(obj, a_class):
    """
    Returns true if obj inherits from the aclass
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
