#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list)):
        my_list.reverse()
        print("{:d}".format(my_list[num]))
