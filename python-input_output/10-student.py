#!/usr/bin/python3
"""This module defines a Student class with filtered JSON"""


class Student:
    """Defines a student with first name, last name and age"""

    def __init__(self, first_name, last_name, age):
        """Sets first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict of Student, filtered by attrs if provided"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
