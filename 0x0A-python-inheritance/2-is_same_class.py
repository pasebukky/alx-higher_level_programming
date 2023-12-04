#!/usr/bin/python3
""" Define a function """


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the given class.
    Args:
        obj: the object to check
        a_class: the class the object is compared with
    Retruns:
        True if type(obj) is equal to a_class; otherwise false
    """
    if type(obj) is a_class:
        return True
    return False
