#!/usr/bin/python3
"""Locked class to dynamically create new instance attribute"""


class LockedClass:
    """ LockedClass Blueprint of instance attribute"""
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
