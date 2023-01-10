#!/usr/bin/python3
"""Module 10-student.
Creates a Student class.
"""


class Student:
    """ public attributes, first_name, last_name, age """

    def __init__(self, first_name, last_name, age):
        """ initializing student instance """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation of student instance """

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for xin attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
