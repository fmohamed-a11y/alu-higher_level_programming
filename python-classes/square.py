#!/usr/bin/python3


class Square:
    """Defines a square with a validated prvate size attribue"""

    def __init__(self, size=0):
        """Sets the size with tyep and value validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
