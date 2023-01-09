#!/usr/bin/python3
""" module - check attribute to be added to object """


def add_attribute(an_obj, an_attr, a_value):
    """ checks attribute of value to add on obj """

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
