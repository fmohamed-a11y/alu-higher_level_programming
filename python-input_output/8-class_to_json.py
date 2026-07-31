#!/usr/bin/python3
"""This module defines a class_to_json function"""


def class_to_json(obj):
    """Returns dictionary representation of an object for JSON serialization"""
    return obj.__dict__
