#!/usr/bin/python3
""" Define a class BaseGeometry """


class BaseGeometry:
    """ Define a public instance method: area """
    def area(self):
        raise Exception("area() is not implemented")

    """
    Define a public instance method: integer_validator
    Args:
        name: is always a string
        value: is always a string
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
