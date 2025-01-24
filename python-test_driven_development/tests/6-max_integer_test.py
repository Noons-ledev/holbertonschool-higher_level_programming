#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_real_list_of_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_list_with_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])


if __name__ == "__main__":
    unittest.main()
