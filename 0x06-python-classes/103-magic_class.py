#!/usr/bin/python3
"""module giving a specific bytecode"""


import math


class MagicClass:
    """"Class giving a specific bytecode"""
    def __init__(self, radius=0):
        """method launched at the creation of the object"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """return the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """return the circumference of the circle"""
        return 2 * math.pi * self.__radius
