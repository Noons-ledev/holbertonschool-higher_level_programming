#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not my_list:
        my_list = []
    for element in my_list:
        print("{:d}".format(element))
