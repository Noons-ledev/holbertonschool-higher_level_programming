#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, integer in enumerate(row):
            if index != len(row) - 1:
                print("{:d}".format(integer), end=" ")
            else:
                print("{:d}".format(integer), end="")
        print()
