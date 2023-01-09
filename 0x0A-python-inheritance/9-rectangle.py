#!/usr/bin/python3
""" module - base geometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ Rectangle inheriting from BaseGeometry """

    def __init__(self, width, height):
        """ Initializing instance with args: wdth and height of rectangle """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Returns a formatted string """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ area of instance Rectangle """

        return self.__width * self.__height
