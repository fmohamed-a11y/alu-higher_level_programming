#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def setUp(self):
        """Resets __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Tests automatic id assignment"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_auto_id_increment(self):
        """Tests automatic id increments"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_given_id(self):
        """Tests saving passed id"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Tests to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Tests to_json_string with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Tests to_json_string with a list"""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_to_json_string_returns_string(self):
        """Tests to_json_string returns a string"""
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(type(result), str)

    def test_from_json_string_none(self):
        """Tests from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Tests from_json_string with empty string"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list(self):
        """Tests from_json_string with a JSON string"""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)

    def test_from_json_string_returns_list(self):
        """Tests from_json_string returns a list"""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(type(result), list)


if __name__ == '__main__':
    unittest.main()
