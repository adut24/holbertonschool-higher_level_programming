#!/usr/bin/python3
"""
module 4-square
"""
class Square:
    """
    class Square defining a square by size
    """
    def __init__(self, size=0):
        """
        method called when the instance is created
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        return the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        return the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        change the size of the square
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')
