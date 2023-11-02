#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer  # Import your max_integer function

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_non_empty_list(self):
        # Test with a non-empty list
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_empty_list(self):
        # Test with an empty list
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
        # Test with a list containing a single element
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_duplicates(self):
        # Test with a list containing duplicate elements
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()
