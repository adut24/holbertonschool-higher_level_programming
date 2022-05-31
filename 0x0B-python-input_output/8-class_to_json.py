#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """return the dictionary description of an object"""
    return obj.__dict__
