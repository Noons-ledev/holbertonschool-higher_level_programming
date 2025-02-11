#!/usr/bin/python3
"""
Module Documentation
"""
import json
"""
Crucial for serialization
"""


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding='utf8') as file:
        file.write(json.dumps(data))
    print("The data has been serialized and saved to {}".format(filename))


def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf8') as file:
        text = file.read()
    return json.loads(text)
