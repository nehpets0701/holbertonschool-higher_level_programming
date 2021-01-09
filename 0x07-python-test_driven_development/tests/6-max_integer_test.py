#!/usr/bin/python3
"""Unittests"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """all tests cases"""
    def test_integers(self):
        """proper input"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([2]), 2)

    def test_strings(self):
        """string"""
        self.assertEqual(max_integer("string"), "a")
        self.assertEqual(max_integer(["string1", "string2"]), "string")

    def test_empty(self):
        """empty"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([[]]), [])

    def test_error(self):
        """wrong type"""
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, None)
