#!/usr/bin/python3
def convert_up(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def uppercase(str):
    new = ""
    for character in str:
        new += "%c" % convert_up(character)
    print("{:s}".format(new))
