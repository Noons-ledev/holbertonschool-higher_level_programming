#!/usr/bin/python3
"""
This module can be used to
indent a text depending on punctuation.
"""


def text_indentation(text):
    """
    checks first if the arg is a string
    then perform to print it
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    Marks = ".?:"
    for i in range(len(text)):
        if text[i] not in Marks:
            print(text[i], end="")
        else:
            print(text[i])
            print()
