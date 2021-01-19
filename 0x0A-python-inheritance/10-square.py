#!/usr/bin/python3
"""geometry class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square based on rectangle"""
    def __init__(self, size):
        """initializes with size"""
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
