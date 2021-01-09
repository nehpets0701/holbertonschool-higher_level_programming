#!/usr/bin/python3
"""adds a + b"""


def add_integer(a, b=98):
    """adds a + b"""
    if type(a) is not int or float:
        raise TypeError("a must be an integer")
    if type(b) is not int or float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
