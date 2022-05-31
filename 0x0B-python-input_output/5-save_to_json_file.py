#!/usr/bin/python3
"""save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""
    with open(filename, 'wt', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
