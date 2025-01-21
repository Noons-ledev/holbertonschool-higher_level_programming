#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = []
    for x in set_1:
        if x not in set_2:
            my_list.append(x)
    for y in set_2:
        if y not in set_1:
            my_list.append(y)
    myset = set(my_list)
    return (myset)
