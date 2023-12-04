#!/usr/bin/python3
""" Create a class MyInt """


class MyInt(int):
    def __new__(cls, value):
        """ Regular init """
        return super(MyInt, cls).__new__(cls, value)

    def __eq__(self, other):
        """ invert the value of equals to """
        return int(self) != other

    def __ne__(self, other):
        """ invert the value of not equal to """
        return int(self) == other
