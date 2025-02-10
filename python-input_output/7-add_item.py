#!/usr/bin/python3
"""
Module Documenation
"""
import sys, json
"""
Handling arguments
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
Using this function inside my program
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Using this function inside my program
"""
filename = 'add_item.json'
try:
    mylist = list(load_from_json_file(filename))
except Exception:
    mylist = []

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        mylist.append(sys.argv[i])
save_to_json_file(mylist, filename)
