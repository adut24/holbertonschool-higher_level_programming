#!/usr/bin/python3
"""Module 5-rectangle"""


class Rectangle:
    """define a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set a new value to width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set a new value to height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """return the rectangle to print"""
        ch = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ch += '#'
            ch += '\n'
        return ch[:-1]

    def __repr__(self):
        """return the command to create the same rectangle"""
        s = 'Rectangle(' + str(self.__width) + ', ' + str(self.__height) + ')'
        return s

    def __del__(self):
        """delete the current Rectangle"""
        print(f"Bye rectangle...")
