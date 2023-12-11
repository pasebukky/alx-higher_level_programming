#!/usr/bin/python3
""" Unittest for square """

import unittest
from models.square import Square


""" Create a class SquareTest """


class TestSquare(unittest.TestCase):
    """ Define unittest for square model """
    def test_initialization_without_arguments(self):
        self.assertRaises(TypeError, Square)


if __name__ == '__main__':
    unittest.main()
