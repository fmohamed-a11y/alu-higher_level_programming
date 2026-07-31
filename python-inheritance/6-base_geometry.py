#!/usr/bin/python3
"""This module defines a BaseGeometry class with area method"""


class BaseGeometry:
    """Base class for geometry with unimplemented area method"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")
