#!/usr/bin/python3
"""
This module is used
to print a square of # signs
just import the function print_square
"""


def print_square(size):
    """
    depending on size
    checking if it's an integer
    if not, raising an error
    then performing the print
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for i in range(size):
            print("#", end="")
        print()
