#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """tell if a object inherited from another class"""
    return issubclass(type(obj), a_class)
