#!/usr/bin/python3
"""
2-matrix_divided.py module
This module is used to divide all elements of a matrix
Different tests will be performed
"""


def matrix_divided(matrix, div):
    """
    divide all elements of a matrix
    """
    length = 0
    for i in range(len(matrix)):
        if i != 0 and len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        length = len(matrix[i])
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    a = matrix.copy()
    for i in range(len(a)):
        a[i] = matrix[i].copy()
        for j in range(len(a[i])):
            if not isinstance(a[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
            a[i][j] = round(a[i][j] / div, 2)
    return a
