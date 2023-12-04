#!/usr/bin/python3
""" Define the function """


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args:
        obj: the object to be checked
        a_class: the class to compare it to
    Return:
        True if its has been inherited and False otherwise
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
