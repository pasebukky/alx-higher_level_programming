#!/usr/bin/python3
""" Define a class named Square """


class Square:
    """ Initialize an instance square """
    def __init__(self, size=0, position=(0, 0)):
        """
        Create an instance of Square
        Args:
            size (int) : size of the square
            position (int, int) : shows the x and y coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Set the value of private size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Set the value of private position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ Prints a square using # at the current position """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
