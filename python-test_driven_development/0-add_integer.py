#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Add two integers or floats, casting floats to int first.

    Args:
        a: first number, int or float
        b: second number, int or float, defaults to 98

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is not an int or float
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
