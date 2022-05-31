#!/usr/bin/python3
"""student module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve a dictionary representation of the instance"""
        return self.__dict__
