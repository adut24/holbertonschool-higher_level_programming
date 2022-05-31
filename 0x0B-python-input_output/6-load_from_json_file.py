#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """create an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        a = json.loads(f.read())
    return a
