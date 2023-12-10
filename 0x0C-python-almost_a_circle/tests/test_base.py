#!/usr/bin/python3
""" Unittests for base class """

import unittest
from models.base import Base


""" Create a test base class """


class TestBase(unittest.TestCase):
    """ Define all the unittests for the Base model """
    def test_id_assignment(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_incremental_id(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
