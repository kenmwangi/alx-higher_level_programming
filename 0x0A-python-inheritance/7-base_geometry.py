#!/usr/bin/python3
""" module - base geometry """

class BaseGeometry:
    """ public instance method """

    def area(self):
        """ Raising exception with message """

        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """ Validates value """
        
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
