#!/usr/bin/python3
"""

Real definition of rectangle with private instances

"""


class Rectangle:
    """ Blueprint of rectangle object"""
    def __init__(self, width=0, height=0):
        """ Object constructor method"""
        self.width = width
        self.height = height

    # instance of width
    @property
    def width(self):
        """ Retrieving private attribute value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width private attribute value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # instance of height
    @property
    def height(self):
        """ Get height private attribute value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height private attribute value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
