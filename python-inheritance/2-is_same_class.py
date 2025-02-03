#!/usr/bin/python3
"""
This module introduces the is same class function
"""


def is_same_class(obj, a_class):
    """
    returns true if obj is of the same class of a_class
    """
    return (type(obj) is a_class)
