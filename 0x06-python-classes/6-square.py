#!/usr/bin/python3
"""Square Class

module defining class Square

"""


class Square:
    """
    blueprint of a square

    size (int) - integer representing object size
    position (int, int)
    """

    def __init__(self, size=0, position=(0,0)):
        """ Object constructor method """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size private attribute
        args: value to be set

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        position private attribute value

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position private attribute value
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        """
        object method
        current square area
        """
        return self.__size**2

    def my_print(self):
        """ Square object with # character"""
        if self.__size = 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
