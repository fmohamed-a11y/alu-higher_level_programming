#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        """Resets __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle_1_2(self):
        """Tests Rectangle(1, 2)"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_1_2_3(self):
        """Tests Rectangle(1, 2, 3)"""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4(self):
        """Tests Rectangle(1, 2, 3, 4)"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_string_width(self):
        """Tests Rectangle with string width"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_width_must_be_integer(self):
        """Tests width must be integer"""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_height_must_be_integer(self):
        """Tests height must be integer"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1.5)

    def test_x_must_be_integer(self):
        """Tests x must be integer"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1.5)

    def test_y_must_be_integer(self):
        """Tests y must be integer"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 1.5)

    def test_width_gt_0(self):
        """Tests width must be > 0"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_gt_0(self):
        """Tests height must be > 0"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_gte_0(self):
        """Tests x must be >= 0"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_gte_0(self):
        """Tests y must be >= 0"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1)

    def test_area(self):
        """Tests area method"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Tests __str__ method"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")


if __name__ == '__main__':
    unittest.main()
