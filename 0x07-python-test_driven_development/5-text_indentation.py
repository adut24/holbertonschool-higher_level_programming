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
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in new_line:
            print(text[i])
        elif text[i] == ' ' and text[i - 1] in new_line:
            print()
        else:
            print(text[i], end="")
