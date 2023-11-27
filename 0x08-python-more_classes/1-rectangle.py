#!/usr/bin/python3
""" Define a class Rectangle """


class Rectangle:
    """ Define width and height of Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initialize the Rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Gets the width of a Rectangle instance """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of a Rectangle instance
        Args:
            value: value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of a Rectang;e instance """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of a Rectangle instance
        Args:
            value: value of the height
        """
        if not isinstance(value, int):
            return TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
