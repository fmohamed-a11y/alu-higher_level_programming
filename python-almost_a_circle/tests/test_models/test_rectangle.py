#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
import os
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

    def test_rectangle_neg_width(self):
        """Tests Rectangle(-1, 2)"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_neg_height(self):
        """Tests Rectangle(1, -2)"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_create_id(self):
        """Tests Rectangle.create with id"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Tests Rectangle.create with id and width"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.width, 1)

    def test_save_to_file_none(self):
        """Tests Rectangle.save_to_file with None"""
        Rectangle.save_to_file(None)

    def test_save_to_file_empty(self):
        """Tests Rectangle.save_to_file with empty list"""
        Rectangle.save_to_file([])

    def test_save_to_file_list(self):
        """Tests Rectangle.save_to_file with a Rectangle"""
        Rectangle.save_to_file([Rectangle(1, 2)])

    def test_load_from_file_no_file(self):
        """Tests Rectangle.load_from_file when file doesnt exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_exists(self):
        """Tests Rectangle.load_from_file when file exists"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        result = Rectangle.load_from_file()
        self.assertIsInstance(result, list)

    def test_display_no_x_no_y(self):
        """Tests display without x and y"""
        r = Rectangle(2, 3)
        r.display()

    def test_display_no_y(self):
        """Tests display without y"""
        r = Rectangle(2, 3, 1)
        r.display()

    def test_display(self):
        """Tests display with x and y"""
        r = Rectangle(2, 3, 1, 1)
        r.display()

    def test_to_dictionary(self):
        """Tests to_dictionary method"""
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()
