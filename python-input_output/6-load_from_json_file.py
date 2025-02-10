#!/usr/bin/python3
"""
Module documentation
"""
import json
"""
To load the json string
"""


def load_from_json_file(filename):
    """
    Function doc
    """
    with open(filename, 'r', encoding='utf8') as file:
        text = file.read()
    return json.loads(text)
