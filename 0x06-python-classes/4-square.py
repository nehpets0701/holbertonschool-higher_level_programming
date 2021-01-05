#!/usr/bin/python3
"class"


class Square:
    "class"
    def __init__(self, size=0):
        "function"
        self.__size = size

    def area(self):
        "function"
        return (self.__size * self.__size)

    @property
    def size(self):
        "function"
        return (self.__size)

    @size.setter
    def size(self, value):
        "function"
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
