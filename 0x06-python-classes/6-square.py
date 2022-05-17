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
        self.__position = position

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
        if type(value) is not tuple and len(value) != 2 and\
        type(value[0]) is not int and type(value[1]) is not int and\
        value[0] < 0 and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
