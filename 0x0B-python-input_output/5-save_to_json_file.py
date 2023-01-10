#!/usr/bin/python3
""" object represented as JSON string """

import json

def save_to_json_file(my_obj, filename):
    """ returns object represented as str """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
