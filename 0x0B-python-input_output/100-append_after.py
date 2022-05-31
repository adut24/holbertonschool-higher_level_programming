#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text to a file"""
    with open(filename, 'rt', encoding='utf-8') as f:
        text = f.readlines()
    with open(filename, 'wt', encoding='utf-8') as f:
        for line in text:
            if search_string in line:
                line += new_string
            f.write(line)
