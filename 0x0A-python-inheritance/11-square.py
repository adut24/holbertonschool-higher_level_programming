#!/usr/bin/python3
"""square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """constructor method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """return an informal string"""
        s = f'[Square] {self.__size}/{self.__size}'
        return s
