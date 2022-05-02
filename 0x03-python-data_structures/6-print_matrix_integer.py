#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join(['{}'.format(n) for n in row])
     for row in matrix]))
