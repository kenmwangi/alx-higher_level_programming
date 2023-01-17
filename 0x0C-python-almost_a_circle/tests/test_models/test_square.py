#!/usr/bin/python3
"""Unittest Square
Test cases for the class Square.
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """class TestSquare that inherits from unittest.TestCase"""

    def setUp(self):
        Base._base__nb_objects = 0

    def test_3_0(self):
        """class TestSquare: checks for attributes."""

        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        s2 = Square(5, 3, 2, 8)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 8)

    def test_3_1(self):
        """class TestSquare: checks for __str__representation."""

        s1 = Square(3, 2, 1, 5)
        self.assertEqual(str(s1), "[Square] (5) 2/1 - 3")

    def test_3_2(self):
        """class TestSquare: checks for inheritence."""

        s1 = Square(3)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_3_3(self):
        """class TestSquare: checks for missing args."""

        with self.assertRaises(TypeError) as x:
            s1 = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                x.exception))

    def test_3_4(self):
        """Test for methods inherited from Rectangle."""

        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(3, 1, 3)
        s2.update(8)
        self.assertEqual(s2.id, 8)
        f = io.StringIO()
        s3 = Square(3)
        with contextlib.redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        res = "###\n###\n###\n"
        self.assertEqual(s, res)

    def test_3_5(self):
        """class TestSquare: checks for size attribute."""

        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 = Square(3, 2, 4, 7)
        self.assertEqual(s2.size, 3)

    def test_3_6(self):
        """class TestSquare: check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            s1 = Square("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))

    def test_3_7(self):
        """Test for public method update."""

        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def test_3_8(self):
        """Test for public method update with wrong types."""

        s1 = Square(5)
        with self.assertRaises(TypeError) as x:
            s1.update("Hello", 5, 3)
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s1.update(4, "world", 3, 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s1.update(1, 2, 2, "Bar")
        self.assertEqual("x must be an integer", str(x.exception))

    def test_3_9(self):
        """Test for public method to_dictionary."""

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s2_dictionary), len(s1_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

    def test_3_10(self):
        """Test for public method to_dictionary with wrong args."""
        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            s1 = Square(10, 2, 1, 9)
            s1_dictionary = s1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
