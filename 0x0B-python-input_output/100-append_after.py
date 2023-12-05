#!/usr/bin/python3
""" Define a function """


def append_after(filename="", search_string="", new_string=""):
    """
    Create a function that inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename: the name of the file
        search_string: string to be replaced
        new_string: new string to be replaced with
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as g:
        g.write(text)
