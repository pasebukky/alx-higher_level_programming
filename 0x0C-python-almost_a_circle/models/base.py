#!/usr/bin/python3
""" Define a class named Base """
import json
import csv
import turtle


class Base:
    """ Define a private class attribute """
    __nb_objects = 0
    """
    Define a class constructor:
    Args:
        id : the identity
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()

            list_of_dicts = json.loads(json_string)

            instances = [cls.create(**dictionary) for dictionary
                         in list_of_dicts]
            return instances

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                         obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of class instantiated from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        if list_rectangles is None:
            list_rectangles = []
        if list_squares is None:
            list_squares = []

        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
