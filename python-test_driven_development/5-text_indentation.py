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
        if text[i] in Marks:
            print(text[i])
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
            print()
        else:
            print(text[i], end="")
