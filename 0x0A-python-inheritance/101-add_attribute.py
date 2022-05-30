#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, key, value):
    """add a new attribute to an object if it's possible"""
    try:
        setattr(obj, key, value)
    except Exception:
        raise TypeError("can't add new attribute")
