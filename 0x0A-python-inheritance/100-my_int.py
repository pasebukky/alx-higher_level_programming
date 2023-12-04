#!/usr/bin/python3
""" Create a class MyInt """


class MyInt(int):
    def __eq__(self, value):
        """ invert the value of equals to """
        return self.real != value

    def __ne__(self, value):
        """ invert the value of not equal to """
        return self.real == value
