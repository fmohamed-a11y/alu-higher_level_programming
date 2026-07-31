#!/usr/bin/python3
"""This module defines MyList that inherits from list"""


class MyList(list):
    """A list that can print itself sorted"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
