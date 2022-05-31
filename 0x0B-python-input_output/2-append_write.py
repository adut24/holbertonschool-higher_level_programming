#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """append text"""
    nb = 0
    with open(filename, 'at', encoding='utf-8') as f:
        nb = f.write(text)
    return nb
