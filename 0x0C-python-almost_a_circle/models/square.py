#!/usr/bin/python3
""" Import Rectangle """

from models.rectangle import Rectangle


""" Define a class named Square """


class Square(Rectangle):
    """ Define a class constructor """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Return the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Assign values to the width and height """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return a defined string """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ Assign attributes """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
