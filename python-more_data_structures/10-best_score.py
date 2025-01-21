#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    max = 0
    key = ""
    for x in a_dictionary:
        if a_dictionary[x] > max:
            max = a_dictionary[x]
            key = x
    return key
