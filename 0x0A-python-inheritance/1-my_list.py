#!/usr/bin/python3
""" Create a class named MyList """


class MyList(list):
    """ Define a public instance method """
    def print_sorted(self):
        """ Return sorted list """
        print(sorted(self))
