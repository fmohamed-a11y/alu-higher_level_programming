#!/usr/bin/python3
"""This module defines a full Rectangle class with area and print"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with area and string representation"""

    def __init__(self, width, height):
        """Sets private width and height using integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle description as [Rectangle] width/height"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
