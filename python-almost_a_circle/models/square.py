#!/usr/bin/python3
"""This module defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance

        Args:
            size: the size of the square, used for both width and height
            x: the x coordinate, defaults to 0
            y: the y coordinate, defaults to 0
            id: the id to assign, or None to auto-increment
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size, assigning both width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes via args (in order: id, size, x, y)
        or via kwargs if args is empty
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
