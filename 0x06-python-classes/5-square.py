#!/usr/bin/python3
"""
Square Class

module contains class define a square

"""
class Square:
    """
    Blueprint of a square

    attribute - size of square object

    """
    def __init__(self, size=0):
        """
        Object constructor method

        arg - integer (default = 0)

        """
        self.__size = size

    @property
    def size(self):
        """
        size private attribute value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size private attribute value

        arg: value to be set
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        method - returns area of square
        """
        return self.__size**2
    
    def my_print(self):
        """
        Square object with # character
        """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
