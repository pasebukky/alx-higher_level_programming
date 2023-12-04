#!/usr/bin/python3
""" Define a class Rectangle that inhetits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Call for super class to initialize fields """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return a given text """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
