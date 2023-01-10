#!/usr/bin/python3
""" module - appending string to end of text file """


def append_write(filename="", text=""):
    """ text to filename """

    with open(filename, 'a+') as f:
        return f.write(text)
