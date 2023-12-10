#!/usr/bin/python3
""" Define a class named Base """
import json
import csv


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation of list_objs to a file """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        list_of_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_of_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

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
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    return [cls.create(id=int(row[0]), width=int(row[1]),
                            height=int(row[2]), x=int(row[3]), y=int(row[4]))
                            for row in reader]
                elif cls.__name__ == "Square":
                    return [cls.create(id=int(row[0]), size=int(row[1]),
                            x=int(row[2]), y=int(row[3])) for row in reader]
        except FileNotFoundError:
            return []
