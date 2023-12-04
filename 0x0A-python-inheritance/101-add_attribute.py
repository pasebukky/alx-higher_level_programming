#!/usr/bin/python3
""" Create a function that adds a new attribute to an object if possible """


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
