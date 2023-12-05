#!/usr/bin/python3
""" Define a function write_file """


def write_file(filename="", text=""):
    """
    The function writes a string to a text file (UTF8)
    Args:
        filename: The name of the file
        text: The content of the file
    Return: The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
