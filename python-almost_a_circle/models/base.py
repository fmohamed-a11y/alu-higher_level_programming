#!/usr/bin/python3
"""This module defines the Base class"""
import json


class Base:
    """Base class for managing id attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Sets id automatically or uses given id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list from a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
