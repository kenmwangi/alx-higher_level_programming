#!/usr/bin/python3
"""Module 9-student.
Creates a Student class.
"""


class Student:
    """ defining student - public attributes (first_name, last_name, age) """

    def __init__(self, first_name, last_name, age):
        """ initializes Student instance """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieve dictionary reprensentation of student instance """

        return self.__dict__
