#!/usr/bin/python3
"""outside class"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """init function"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """function"""
        return self.__size

    @size.setter
    def size(self, value):
        """function that sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """function that gets position"""
        return self.__position

    @position.setter
    def position(self, value):
        """function that sets possition"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates area"""
        return self.__size * self.__size

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__position[0]):
                        print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
