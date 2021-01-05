#!/usr/bin/python3
"class comment outside"


class Square:
    "Square class"
    def __init__(self, size=0):
        "function to initialize size"
        self.__size = size

    def area(self):
        "function to calculate area"
        return (self.__size * self.__size)

    @property
    def size(self):
        "function to get size"
        return (self.__size)

    @size.setter
    def size(self, value):
        "function to set size"
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
