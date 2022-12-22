#!/usr/bin/python3
"""Module for add_integer function"""

def add_integer(a, b=98):
    """Adding two integers

    arguments - a (int) & b (int)

    TypeError - a, b neither int or float
    Returns - sum(a,b)
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
