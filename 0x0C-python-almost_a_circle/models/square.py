#!/usr/bin/python3
"""square class that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherits from rectangle"""
    def __init__(self, size=None, x=0, y=0, id=None):
        """init square with super"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns width of square"""
        return self.width

    @size.setter
    def size(self, size):
        """sets size of square"""
        self.width = size
        self.height = size

    def __str__(self):
        """returns square as a string"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates attrubutes of square"""
        attributes = ["id", "size", "x", "y"]
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return

        for index in range(len(args)):
            setattr(self, attributes[index], args[index])

    def to_dictionary(self):
        """returns rectangle attributes as dictionary"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
