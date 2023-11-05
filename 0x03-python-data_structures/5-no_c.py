#!/usr/bin/python3
def no_c(my_string):
    result = []
    for char in my_string:
        if char not in 'cC':
            result.append(char)
    new_string = ''.join(result)
    return new_string
