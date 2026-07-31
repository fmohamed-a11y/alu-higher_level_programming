#!/usr/bin/python3
"""This module defines a Square class with getter and setter"""


class Square:
    """Defines a square with getter and setter for size"""

    def __init__(self, size=0):
        """Sets the size using the setter"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
