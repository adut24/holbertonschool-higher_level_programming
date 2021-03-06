#!/usr/bin/python3
"""
5-text_indentation.py module
This module is used to print a text
Different tests will be performed
"""


def text_indentation(text):
    """
    print a text
    """
    new_line = ['.', '?', ':']
    check = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        if c in new_line:
            print(c)
            print()
            check = 1
        else:
            if c == ' ' and check == 1:
                check = 2
                continue
            elif c == ' ' and check == 2:
                continue
            else:
                print(c, end="")
                check = 0
