#!/usr/bin/python3
"""
100-matrix_mul.py module
This module is used to multiply 2 matrixes
Different tests will be performed
"""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrixes"""
    cell = 0
    result = []
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise ValueError('m_a must be a list of lists')
        for j in range(len(m_a[i])):
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError('m_a should contain only integers or floats')
        if i != 0:
            prev_length = len(m_a[i - 1])
            if len(m_a[i]) != prev_length:
                raise TypeError('each row of m_a must be of the same size')
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise ValueError('m_b must be a list of lists')
        for j in range(len(m_b[i])):
            if not isinstance(m_b[i][j], (int, float)):
                raise TypeError('m_b should contain only integers or floats')
        if i != 0:
            prev_length = len(m_b[i - 1])
            if len(m_b[i]) != prev_length:
                raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for i in range(len(m_b[0])):
        for j in range(len(m_a)):
            cell += m_a[i][j] * m_b[j][i]
        result.append(cell)
        cell = 0
    return result
