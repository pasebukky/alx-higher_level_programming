#!/usr/bin/python3
""" Define a function """


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
    Args:
        obj: the object to check
        a_class: the class to compare it to
    Return:
        True if it is and false otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
