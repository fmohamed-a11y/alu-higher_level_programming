#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle that validates width and height"""

    def __init__(self, width, height):
        """Sets private width and height using integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
