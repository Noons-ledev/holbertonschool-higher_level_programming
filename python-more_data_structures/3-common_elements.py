def common_elements(set_1, set_2):
    myset = []
    for i in set_1:
        for j in set_2:
            if i == j:
                myset.append(i)
    my_set = set(myset)
    return (my_set)
