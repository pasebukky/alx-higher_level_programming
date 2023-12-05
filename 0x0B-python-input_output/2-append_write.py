#!/usr/bin/python3
""" Define a function append_write """


def append_write(filename="", text=""):
    """
    The function appends a string at the end of a text file (UTF8)
    Args:
        filename: The name of the file
        text: the text to be appended
    Return: The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
