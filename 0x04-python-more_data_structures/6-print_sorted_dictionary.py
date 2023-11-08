#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_key = list(a_dictionary.keys())
    dic_key.sort()

    for key in dic_key:
        print("{}: {}".format(key, a_dictionary[key]))
