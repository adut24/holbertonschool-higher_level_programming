#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    for k in a:
        a[k] *= 2
    return a
