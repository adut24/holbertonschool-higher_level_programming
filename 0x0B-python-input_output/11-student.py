#!/usr/bin/python3
"""student module"""
import json


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve a dictionary representation of the instance"""
        if attrs is None:
            return json.loads(json.dumps(self.__dict__))
        a = dict({})
        for k, v in self.__dict__.items():
            if k in attrs:
                a.update({k: v})
        return a

    def reload_from_json(self, json):
        """replace all attributes of the instance"""
        for k, v in json.items():
            if k == "first_name":
                self.first_name = v
            elif k == "last_name":
                self.last_name = v
            elif k == "age":
                self.age = v
