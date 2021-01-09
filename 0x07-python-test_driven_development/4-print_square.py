#!/usr/bin/python3
"""prints square"""


def print_square(size):
    """prints square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float:
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print("")
