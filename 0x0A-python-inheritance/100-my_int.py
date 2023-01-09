#!/usr/bin/python3
""" module - creating class to inherit from int """

class MyInt(int):
    """ class inheriting from int"""

    def __eq__(self, other):
        """ Equality becomes inequality """
        
        return super().__ne__(other)

    def __ne__(self, other):
        """ inequality becomes equality """

        return super().__eq__(other)
