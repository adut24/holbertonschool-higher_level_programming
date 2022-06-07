#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set a new width"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set a new height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set a new value to x"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set a new value to y"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """return the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the Rectangle instance"""
        for a in range(self.__y):
            print()
        for b in range(self.__height):
            for c in range(self.__x):
                print(' ', end='')
            for d in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """return a description of the instance"""
        s = f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'
        s += f' - {self.__width}/{self.__height}'
        return s

    def update(self, *args, **kwargs):
        """assign a value to each attribute"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return a dictionary representation"""
        a = {'id': self.id, 'width': self.width, 'height': self.height,
             'x': self.x, 'y': self.y}
        return a
