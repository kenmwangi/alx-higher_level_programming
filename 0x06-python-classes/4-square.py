#!/usr/bin/python3

"""
Square Class

The module contains class defining square

"""


class Square:
    """
    blueprint of a square

    attribute - integer indicating size of square object

    """
    def __init__(self, size=0):
        """
        Constructor method - initializes square size

        arg - size (default 0)
        """
        self.__size = size

    @property
    def size(self):
        """
        return size private attribute

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        private attribute value
        arg - value to be set

        Raises - TypeError - size not integer
               - ValueError - size > 0

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """
        Object method

        returns - square area
        """
        return self.__size**2
