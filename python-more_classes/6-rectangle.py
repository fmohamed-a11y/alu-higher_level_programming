#!/usr/bin/python3
"""This module defines a Rectangle that counts its instances"""


class Rectangle:
    """Defines a rectangle that tracks how many instances exist"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Sets width and height, increments instance counter"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter, 0 if width or height is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the rectangle drawn with # characters"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string that recreates the rectangle via eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints bye and decrements instance counter when deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
