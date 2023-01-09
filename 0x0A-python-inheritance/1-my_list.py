#!/usr/bin/python3
""" Module - class inheriting list class
"""

class MyList(list):
    """ inheriting from list """

    def print_sorted(self):
        """ printing list in ascending order """
        new_list = self[:]
        new_list.sort()
        print(f"{new_list}")
