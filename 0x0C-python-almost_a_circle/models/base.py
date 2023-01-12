#!/usr/bin/python3
""" module - base class for inheritance """

class Base:
    """ private class attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization base instance """

        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
