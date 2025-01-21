#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = {key: a_dictionary[key] for key in sorted(a_dictionary)}
    for key, value in sorted_dic.items():
        print("{}: {}".format(key, value))
