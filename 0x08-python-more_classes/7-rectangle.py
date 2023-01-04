#!/usr/bin/python3
"""

Real definition of rectangle with private instances

"""


class Rectangle:
    """ Blueprint of rectangle object"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Object constructor method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        total = ""
        if self.__height == 0 or self.width == 0:
            return total
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    total += str(self.print_symbol)
                except Exception:
                    total += type(self).print_symbol
            if i is not self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """ Public Object method - returns current rectangle perimeter"""
        return self.__width * self.__height

    def perimeter(self):
        """ public object method - returns current rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)
