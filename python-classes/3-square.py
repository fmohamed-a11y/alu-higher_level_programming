#!/usr/bin/python3
"""This module defines a Square class with an area method"""


class Square:
    """Defines a square with size validation and area calculation"""

    def __init__(self, size=0):
        """Sets the size with type and value validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
