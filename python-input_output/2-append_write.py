#!/usr/bin/python3
"""
module doc
"""


def append_write(filename="", text=""):
    """
    Function doc
    """
    with open(filename, 'a', encoding='utf8') as file:
        file.write(text)
    return len(text)
