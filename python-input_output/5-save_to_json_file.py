#!/usr/bin/python3
"""
Module Doc
"""
import json
"""
useful you'll see
"""


def save_to_json_file(my_obj, filename):
    """
    Function doc
    """
    with open(filename, 'w', encoding='utf8') as file:
        a = json.dumps(my_obj)
        file.write(a)
