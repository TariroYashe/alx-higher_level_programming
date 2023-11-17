#!/usr/bin/python3
import unittest
from models.square import Square  # Import the Square class from your project's module (adjust the import path as needed)


class TestSquare(unittest.TestCase):
    def setUp(self):
        # You can set up any common configurations or objects here
        pass

    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_square_size_property(self):
        square = Square(3)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_square_update_method(self):
        square = Square(2, 1, 2, 10)
        square.update(20, 5, 6, 7)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_square_update_method_with_kwargs(self):
        square = Square(2, 1, 2, 10)
        square.update(id=20, size=5, x=6, y=7)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_square_to_dictionary_method(self):
        square = Square(3, 2, 1, 5)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 5, 'size': 3, 'x': 2, 'y': 1})

    def test_square_str_representation(self):
        square = Square(4, 1, 3, 8)
        expected_str = "[Square] (8) 1/3 - 4"
        self.assertEqual(str(square), expected_str)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
