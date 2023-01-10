#!/usr/bin/python3
""" write text file """


def write_file(filename, text=""):
    """ text in filename """

    with open(filename, 'w+') as f:
        return f.write(text)
