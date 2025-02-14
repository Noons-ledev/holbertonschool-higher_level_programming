#!/usr/bin/python3
"""
Module documentation
"""


def pascal_triangle(n):
    """
    Class documentation
    """
    if n <= 0:
        return []
    matrix = []
    matrix.append([1])
    for i in range(1, n):
        list = [1]
        for j in range(1, i):
            list.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        list.append(1)
        matrix.append(list)
    return matrix
