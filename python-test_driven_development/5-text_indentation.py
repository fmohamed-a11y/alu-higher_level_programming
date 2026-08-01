#!/usr/bin/python3
"""This module defines a text_indentation function"""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    for char in text:
        result += char
        if char in ".?:" and (i + 1 == len(text) or text[i + 1] == " "):
            result += "\n\n"
        i += 1

    lines = result.split("\n")
    for line in lines:
        print(line.strip())
