#!/usr/bin/python3
""" Create a class """


class Student:
    """ Create public instance attributes """
    def __init__(self, first_name, last_name, age):
        """ Initialize instances """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs : The attributes to represent.
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        return (self.__dict__)
