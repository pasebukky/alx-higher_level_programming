#!/usr/bin/python3
""" Create find_peak function """


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_recursive(arr, low, high):
    """
    Find a peak recursion.
    """
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    if arr[mid] > arr[mid + 1]:
        return find_peak_recursive(arr, low, mid)
    else:
        return find_peak_recursive(arr, mid + 1, high)
