#!/usr/bin/python3
""" Define a function """

import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation
    of an object (string)
    """
    return (json.dumps(my_obj))
