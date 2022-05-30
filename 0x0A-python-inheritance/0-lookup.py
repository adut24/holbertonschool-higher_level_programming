#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """function returning a list of the object's attributes and methods"""
    return list(dir(obj))
