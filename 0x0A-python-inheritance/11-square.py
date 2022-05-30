#!/usr/bin/python3
"""square module"""


class BaseGeometry:
    """BaseGeometry class"""
    def integer_validator(self, name, value):
        """validate if it's an integer or not"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


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


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """constructor method"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """return an informal string"""
        s = f'[Square] {self.__size}/{self.__size}'
        return s
