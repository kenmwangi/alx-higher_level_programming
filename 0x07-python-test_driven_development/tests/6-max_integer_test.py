#!/usr/bin/python3

"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function"""

    def test_regular(self):
        """ Test regular list (ints): return max result"""
        l = [1,2,3,4,5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with a list on non-ints and ints"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """Test with an empty list: return NONE"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test list of negative values: returns max"""
        l = [-2,-6,-1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test list of ints and floats; Returns max"""
        l = [2, 2.5, 1]
        result = max_integer(l)
        self.assertEqual(result, 2.5)

    def test_not_list(self):
        """Test parameters not list: raise TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test list of one int: return value of int"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Tesst with a list of identical values"""
        l = [8,8,8,8,8]
        result = max_integer(l)
        self.assertEqual(result, 8)
    def test_strings(self):
        """Test with list of strings: first string"""
        l = ["ken","hello"]
        result = max_integer(l)
        self.assertEqual(result, "ken")

    def test_none(self):
        """Test with a None as parameter; raises TypError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()

