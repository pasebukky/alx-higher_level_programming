#!/usr/bin/python3
""" Unittests for model.rectangle """

import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ Define unittest for Rectangle model """
    def test_inheritance_from_base(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_initialization(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_width_and_height_setters(self):
        r = Rectangle(5, 3)
        r.width = 7
        r.height = 2
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 2)

    def test_str(self):
        r = Rectangle(4, 2, 1, 3, 7)
        expected_str = "[Rectangle] (7) 1/3 - 4/2"
        self.assertEqual(str(r), expected_str)

class TestRectangle_stdout(unittest.TestCase):
    @staticmethod
    def capture_stdout(obj, method, *args, **kwargs):
        """Capture stdout for a method call."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        if method == "print":
            print(obj)
        else:
            getattr(obj, method)(*args, **kwargs)
        sys.stdout = sys.__stdout__
        captured_output.seek(0)
        return captured_output

class TestRectangleValidation(unittest.TestCase):
    """ Define unittest for validation of the Rectangle model """
    def test_invalid_width_and_height_type(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("10", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_invalid_width_and_height_value(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.width = 0
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.height = -5
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.height = 0
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_invalid_x_and_y_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2)
            r.y = {}
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_invalid_x_and_y_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, -3, 0)
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

class TestRectangleArea(unittest.TestCase):
    """ Define unittests for Rectangle class area method """
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

class TestRectangleDisplay(unittest.TestCase):
    """ Define unittests for Rectangle class display method """
    def test_display(self):
        r1 = Rectangle(4, 6)
        expected_output_r1 = "####\n####\n####\n####\n####\n####\n"
        with StringIO() as captured_output:
            sys.stdout = captured_output
            r1.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue(), expected_output_r1)

        r2 = Rectangle(2, 2)
        expected_output_r2 = "##\n##\n"
        with StringIO() as captured_output:
            sys.stdout = captured_output
            r2.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue(), expected_output_r2)

class TestRectangleStr(unittest.TestCase):
    """Define unit tests for Rectangle class __str__ method"""
    def test_str_method_width_and_height(self):
        r = Rectangle(4, 6)

        with TestRectangle_stdout.capture_stdout(r, "print") as captured_output:
            correct_output = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
            self.assertEqual(correct_output, captured_output.getvalue())

        str_representation = str(r)
        correct_output = "[Rectangle] ({}) 0/0 - 4/6".format(r.id)
        self.assertEqual(correct_output, str_representation)

    def test_str_method_width_height_and_x(self):
        r = Rectangle(4, 6, 1)

        with TestRectangle_stdout.capture_stdout(r, "print") as captured_output:
            correct_output = "[Rectangle] ({}) 1/0 - 4/6\n".format(r.id)
            self.assertEqual(correct_output, captured_output.getvalue())
    
        str_representation = str(r)
        correct_output = "[Rectangle] ({}) 1/0 - 4/6".format(r.id)
        self.assertEqual(correct_output, str_representation)

    def test_str_method_width_height_x_and_y(self):
        r = Rectangle(4, 6, 1, 2)

        with TestRectangle_stdout.capture_stdout(r, "print") as captured_output:
            correct_output = "[Rectangle] ({}) 1/2 - 4/6\n".format(r.id)
            self.assertEqual(correct_output, captured_output.getvalue())

        str_representation = str(r)
        correct_output = "[Rectangle] ({}) 1/2 - 4/6".format(r.id)
        self.assertEqual(correct_output, str_representation)

    def test_str_method_width_height_x_y_and_id(self):
        r = Rectangle(4, 6, 1, 2, 5)

        with TestRectangle_stdout.capture_stdout(r, "print") as captured_output:
            correct_output = "[Rectangle] (5) 1/2 - 4/6\n"
            self.assertEqual(correct_output, captured_output.getvalue())

        str_representation = str(r)
        correct_output = "[Rectangle] (5) 1/2 - 4/6"
        self.assertEqual(correct_output, str_representation)

if __name__ == '__main__':
    unittest.main()
