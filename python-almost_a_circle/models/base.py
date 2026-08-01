#!/usr/bin/python3
"""This module defines the Base class"""


class Base:
    """Base class that manages the id attribute for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance

        Args:
            id: the id to assign, or None to auto-increment
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
