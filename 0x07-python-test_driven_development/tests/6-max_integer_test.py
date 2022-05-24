#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class used for unittest for the max_integer function
    """
    def test_max_integer(self):
        """
        function testing max_integer
        """
        test_list = [1, 2, 3, 4]
        self.assertAlmostEqual(max_integer(test_list), 4)
        test_list = []
        self.assertAlmostEqual(max_integer(test_list), None)
        test_list = [-1, 2.67, -3.3, -14, 0.5]
        self.assertAlmostEqual(max_integer(test_list), 2.67)
        test_list = [-12, 0, -23.31231, 24, float("inf")]
        self.assertAlmostEqual(max_integer(test_list), float("inf"))
        test_list = [-1.122, 0.3490, -2, 4, int("1024")]
        self.assertAlmostEqual(max_integer(test_list), 1024)
        test_list = [22, 3.14, -0.232, 4, float("NaN")]
        self.assertAlmostEqual(max_integer(test_list), 22)
        test_list = [-22, -3.14, -0.232, -4, -123]
        self.assertAlmostEqual(max_integer(test_list), -0.232)

    def test_types(self):
        """test the function with different types of data"""
        test_list = ["hello", 0, -23.31231, 1]
        self.assertRaises(TypeError, max_integer, test_list)
        test_list = [int("23"), 0.320, 12, (1, 2)]
        self.assertRaises(TypeError, max_integer, test_list)
        test_list = [1, {'test': 1, 'view': (1, 2)}]
        self.assertRaises(TypeError, max_integer, test_list)
        test_list = [1, {0, "hello"}]
        self.assertRaises(TypeError, max_integer, test_list)
        test_list = None
        self.assertRaises(TypeError, max_integer, test_list)
