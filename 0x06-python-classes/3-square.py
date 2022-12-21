#!/usr/bin/python3
"""
Module Square - defines squares

"""


class Square:
    """
    size - integer instance attribute
    """


    def __init__(self, size=0):
        """
        size - private instance attribute
        TypeError - exception message("must be an integer")
        valueError - exception message("size must be >= 0")
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """
        Public object method

        returns - current square area

        """
        return self.__size**2
