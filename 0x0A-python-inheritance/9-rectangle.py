#!/usr/bin/python3
"""rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """constructor method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return an informal string"""
        s = f'[Rectangle] {self.__width}/{self.__height}'
        return s

    def area(self):
        """area method"""
        return self.__height * self.__width
