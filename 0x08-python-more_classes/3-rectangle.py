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

    def __str__(self):
        """ returning string representation of Rectangle instance"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

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

    def area(self):
        """ Public Object method - returns current rectangle perimeter"""
        return self.__width * self.__height

    def perimeter(self):
        """ public object method - returns current rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)
