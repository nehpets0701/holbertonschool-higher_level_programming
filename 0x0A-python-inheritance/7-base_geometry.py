#!/usr/bin/python3
"""geometry class"""


class BaseGeometry:
    """geometry class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        """validates input"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))