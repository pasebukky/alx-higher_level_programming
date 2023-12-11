#!/usr/bin/python3
""" Import class base """

from models.base import Base


""" Define a class Rectangle """


class Rectangle(Base):
    """ Define a class constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Return width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set private attribute for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Return height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set private attribute for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Return x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set private attribute for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Return y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set private attribute for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the value of area """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """ Return a given text string """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
    """Update the Rectangle instance attributes."""
    attrs = ['id', 'width', 'height', 'x', 'y']
    for i, arg in enumerate(args):
        setattr(self, attrs[i], arg)

    for key, value in kwargs.items():
        if key in attrs:
            setattr(self, key, value)

    def to_dictionary(self):
        """ Returs the dictionary representation of a rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
