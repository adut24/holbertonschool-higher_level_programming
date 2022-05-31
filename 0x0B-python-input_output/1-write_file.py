#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """write in a file"""
    nb = 0
    with open(filename, 'wt', encoding='utf-8') as f:
        nb = f.write(text)
    return nb
