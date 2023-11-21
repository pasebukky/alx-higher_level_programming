#!/usr/bin/python3
""" Define a class named Square """


class Square:
    """ Initialize an instance of square """
    def __init__(self, size=0):
        """
        Create an instance of square
        Args:
            size (int) : the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Initialize an instance for area"""
    def area(self):
        """ Return the current square area """
        return (self.__size * self.__size)
