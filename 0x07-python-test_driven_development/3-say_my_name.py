#!/usr/bin/python3
"""
Module say_my_name
Prints a given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    print first name and last name
    """

    if type(first_name) is not str:
        raise TypeError("first name must be a string")
    if type(last_name) is not str:
        raise TypeError("last name must be a string")

    print(f"My name is {} {}")
