#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def setUp(self):
        """Resets __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_square_1(self):
        """Tests Square(1)"""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        """Tests Square(1, 2)"""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        """Tests Square(1, 2, 3)"""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_string_size(self):
        """Tests Square with string size"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_size_must_be_integer(self):
        """Tests size must be integer"""
        with self.assertRaises(TypeError):
            Square(1.5)

    def test_size_gt_0(self):
        """Tests size must be > 0"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_gte_0(self):
        """Tests x must be >= 0"""
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_y_gte_0(self):
        """Tests y must be >= 0"""
        with self.assertRaises(ValueError):
            Square(1, 2, -1)

    def test_area(self):
        """Tests area method"""
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        """Tests __str__ method"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_size_getter(self):
        """Tests size getter"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Tests size setter"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_update_args(self):
        """Tests update with args"""
        s = Square(1)
        s.update(2, 3, 4, 5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)

    def test_to_dictionary(self):
        """Tests to_dictionary method"""
        s = Square(1, 2, 3, 4)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 4, 'size': 1, 'x': 2, 'y': 3})


if __name__ == '__main__':
    unittest.main()
