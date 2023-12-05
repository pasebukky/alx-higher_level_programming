#!/usr/bin/python3
""" Define a function that reads a text file """


def read_file(filename=""):
    """ Read a file using with statement """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
