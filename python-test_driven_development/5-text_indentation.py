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
    i = 0
    while i < len(text):
        if text[i] in Marks:
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1