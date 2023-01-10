#!/usr/bin/python3
""" module - reading file nd printing contents """


def read_file(filename=""):
    """ reading file """
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
