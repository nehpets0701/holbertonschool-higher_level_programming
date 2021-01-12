#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimiter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """returns rectangle string"""
        recString = ""
        if self.__width == 0 or self.__height == 0:
            recString = "\n"
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    recString += str(self.print_symbol)
                recString += "\n"
        return recString[:-1]

    def __repr__(self):
        """returns string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete object"""
        print("Bye rectangle...")
        self.number_of_instances -= 1
