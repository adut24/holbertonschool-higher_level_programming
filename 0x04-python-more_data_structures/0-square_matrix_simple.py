#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = matrix.copy()
    for i in range(len(a)):
        a[i] = matrix[i].copy()
        for j in range(len(a[i])):
            a[i][j] **= 2
    return a
