#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_ordered_list(self):
        """list in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """list not in order"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """list in descending order"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """empty list returns None"""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """no argument uses default empty list, returns None"""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_mixed_numbers(self):
        """list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 0, 3]), 5)

    def test_same_elements(self):
        """list where all elements are the same"""
        self.assertEqual(max_integer([7, 7, 7]), 7)


if __name__ == "__main__":
    unittest.main()
