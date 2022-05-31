#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """read a file"""
    with open(filename, 'rt', encoding='utf-8') as f:
        print(f.read(), end='')
