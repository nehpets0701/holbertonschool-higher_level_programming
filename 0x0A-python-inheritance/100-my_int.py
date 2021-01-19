#!/usr/bin/python3
"""inherits from int"""


class MyInt(int):
    """New version of int"""
    def __eq__(self, other):
        """check if equal"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """check if not equal"""
        return int.__eq__(self, other)
