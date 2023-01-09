#!/usr/bin/python3
""" module - find if objet has same instance as class """

def is_same_class(obj, a_class):
    """ function to check class is instance of a class """
    return True if type(obj) is a_class else False
