#!/usr/bin/python3

from task import add

"""
Addition function from file add_0.py

Args: a: first integer, b: second integer

Returns value. a + b
"""

a = 1
b = 2

if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
