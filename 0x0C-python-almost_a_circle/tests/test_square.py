#!/usr/bin/python3
""" Unittest for square """

import unittest
from models.square import Square


""" Create a class SquareTest """


class TestSquare(unittest.TestCase):
    """ Define unittest for square model """
    def test_initialization(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 2)
        self.assertEqual(s2.id, 2)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.id, 3)

    def test_initialization_without_arguments(self):
        self.assertRaises(TypeError, Square)


if __name__ == '__main__':
    unittest.main()
