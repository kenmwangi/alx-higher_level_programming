#!/usr/bin/python3
""" object represented as JSON string """

import json

def from_json_string(my_str):
    """ returns object represented as str """

    return json.loads(my_str)
