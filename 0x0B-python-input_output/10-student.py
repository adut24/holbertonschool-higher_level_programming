#!/usr/bin/python3
"""student module"""


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
            return self.__dict__
        a = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                a.update({k: v})
        return a
