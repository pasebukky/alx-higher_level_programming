#!/usr/bin/python3
""" Create find_peak function """


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    peak = list_of_integers[0]

    for num in list_of_integers:
        is_peak = True

        for neighbor in list_of_integers:
            if neighbor > num:
                is_peak = False
                break

        if is_peak:
            peak = num
            break

    return peak
