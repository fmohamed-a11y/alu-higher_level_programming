#!/usr/bin/python3
"""This module defines inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True only if obj inherited from a class, not the class itself"""
    return isinstance(obj, a_class) and type(obj) is not a_class
