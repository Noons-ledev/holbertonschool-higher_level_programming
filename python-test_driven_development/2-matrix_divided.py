#!/usr/bin/python3
def matrix_divided(matrix, div):
    check = True
    Same_len = True
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if row_len != len(row):
            Same_len = False
        for a in row:
            if not isinstance(a, (int, float)):
                check = False
    if not check:
        raise TypeError("matrix must be a matrix (list of lists) "\
           "of integers/floats")
    if not Same_len:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = [[round(x / div, 2) for x in row]for row in matrix]
    return new_matrix
