#!/usr/bin/python3
"""
Module Square

size - private instance attribute

"""
class Square:
    """
    size instance - integer

    check exceptions using TypeError with message "size must be an integer"
    size 0 - ValueError. size must be >= 0

    """
    def __init__(self, size=0):
        """
        Object constructor method

        arg - size (integer)

        Raises:
        TypeError - size not integer
        ValueEror - size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
