#!/usr/bin/python3
""" Module - finding object is istance of class inherited """

def inherits(obj, a_class):
    """ determine of obj is instance of class inherited """
    return isinstance(obj, a_class) and type(obj) != a_class
