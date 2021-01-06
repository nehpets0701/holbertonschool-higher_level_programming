#!/usr/bin/python3
"""Class outside"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """function to init size"""
        self.__size = size

    @property
    def size(self):
        """function to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """function to set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """function to calculate area"""
        return self.__size * self.__size

    def my_print(self):
        """prints square"""
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
