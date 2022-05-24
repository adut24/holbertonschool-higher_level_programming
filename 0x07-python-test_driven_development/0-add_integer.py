#!/usr/bin/python3
"""
0-add_integer.py module
This module is used to add two integers
Different tests will be performed
"""


def add_integer(a, b=98):
    """
    function adding two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
