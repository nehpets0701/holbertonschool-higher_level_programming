#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """true/false"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
