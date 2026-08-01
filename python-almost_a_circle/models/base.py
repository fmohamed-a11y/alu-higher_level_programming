#!/usr/bin/python3
"""Defines the Base class."""

import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
