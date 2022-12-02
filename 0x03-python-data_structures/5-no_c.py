#!/usr/bin/python3
def no_c(my_string):
    """
    Removing all characters c and C from a string
    """
    dict = {ord(char): None for char in "cC"}

    new_string = my_string.translate(dict)
    return new_string
