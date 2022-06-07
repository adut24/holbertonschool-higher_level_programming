#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a representation of the square"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """return the size"""
        return self.width

    @size.setter
    def size(self, size):
        """set a new size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update the value of the instance"""
        attr = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return a dictionary representation"""
        a = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return a
