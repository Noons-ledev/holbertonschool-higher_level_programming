#!/usr/bin/python3
"""
Module documentation
"""
import csv
import json
"""
Mandatory for the following process
"""


def convert_csv_to_json(filename):
    """
    Class documentation
    """
    try:
        with open(filename, 'r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        with open('data.json', 'w', encoding='utf8') as fileto:
            datato = json.dumps(data)
            fileto.write(datato)
        return True
    except Exception:
        return False
