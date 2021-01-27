#!/usr/bin/python3
"""rectangle - inherits from base"""
from models.base import Base


class Rectangle(Base):
    """rectangle - inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets width and returns it"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets width and handles exceptions"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """gets height and returns it"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets height and handles exceptions"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """gets x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets x coordinate of rectangle"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """gets y coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y coordinate of rectangle"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """calulates area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                    print(' ', end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """returns a printable string rep of our rectangle"""
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return

        for i in range(len(args)):
            setattr(self, attributes[index], args[index])

    def to_dictionary(self):
        """returns rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
