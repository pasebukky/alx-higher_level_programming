#!/usr/bin/python3
""" Define a class Rectangle that inhetits from BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Call for super class to initialize fields """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """ Return the area of the square """
        return self.__size * self.__size
