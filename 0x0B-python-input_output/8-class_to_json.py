#!/usr/bin/python3
"""class_to_json module"""
import json


def class_to_json(obj):
    """return the dictionary description of an object"""
    return json.loads(json.dumps(obj.__dict__))
