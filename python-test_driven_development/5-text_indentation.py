#!/usr/bin/python3
"""This module defines a text_indentation function"""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        if char in ".?:":
            result += char + "\n\n"
        else:
            result += char

    lines = [line.strip() for line in result.split("\n")]
    print("\n".join(lines), end="")
