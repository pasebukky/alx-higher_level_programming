#!/usr/bin/python3
""" Define a function """

import json


def load_from_json_file(filename):
    """ Create  a function that creates an Object from a “JSON file” """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
