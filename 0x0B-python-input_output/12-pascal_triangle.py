#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    """return the pascal triangle as a list"""
    a = []
    if n <= 0:
        return a
    row = []
    prev_row = []
    for i in range(n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and prev_row[j-1] + prev_row[j]\
            or 1 for j in range(i)]
        prev_row = row
        a += [row]
    return a[1:]
