#!/usr/bin/python3
"""
module 6-square
"""


class Square:
    """
    class Square defining a square by size
    """
    def __init__(self, size=0, position=(0, 0)):
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
        if isinstance(position, tuple) and len(position) == 2 and\
            isinstance(position[0], int) and isinstance(position[1], int) and\
                position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

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

    def my_print(self):
        """
        print the square
        """
        if self.__size == 0:
            print()
            return
        for a in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """
        return the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        change the position of the square
        """
        if isinstance(value, tuple) and len(value) == 2 and\
            isinstance(value[0], int) and isinstance(value[1], int) and\
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
