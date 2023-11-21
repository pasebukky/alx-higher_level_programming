#!/usr/bin/python3
""" Define a class named Square """


class Square:
    """ Initialize an instance square """
    def __init__(self, size=0):
        """
        Create an instance of Square
        Args:
            size (int) : size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Set the value of private size attribute """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the current square area """
        return (self.__size * self.__size)
