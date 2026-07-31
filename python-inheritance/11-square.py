#!/usr/bin/python3
"""This module defines a Square class with custom string representation"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that prints itself as [Square] width/height"""

    def __init__(self, size):
        """Sets private size using integer_validator"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns square description as [Square] size/size"""
        return "[Square] {}/{}".format(self.__size, self.__size)
