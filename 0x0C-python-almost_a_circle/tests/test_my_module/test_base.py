#!/usr/bin/python3

import unittest
from models.base import Base, YourClassName, ShapeDrawer


class TestBase(unittest.TestCase):

    def test_base_instance_creation(self):
        # Test if Base instance is created with a unique ID
        base_instance_1 = Base()
        base_instance_2 = Base()

        self.assertNotEqual(base_instance_1.id, base_instance_2.id)

    def test_base_id_with_custom_id(self):
        # Test if Base assigns the provided ID
        custom_id = 42
        base_instance = Base(id=custom_id)

        self.assertEqual(base_instance.id, custom_id)


class TestYourClassName(unittest.TestCase):

    def test_to_json_string_with_empty_list(self):
        # Test if to_json_string returns an empty JSON array string for an empty list
        result = YourClassName.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_valid_list(self):
        # Test if to_json_string serializes a list of dictionaries correctly
        input_list = [{"key1": "value1"}, {"key2": "value2"}]
        expected_result = '[{"key1": "value1"}, {"key2": "value2"}]'

        result = YourClassName.to_json_string(input_list)

        self.assertEqual(result, expected_result)

    def test_save_to_file_with_none_list(self):
        # Test if save_to_file writes an empty list to the file for None input
        with unittest.mock.patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            YourClassName.save_to_file(None)

        mock_file().write.assert_called_once_with("[]")

    def test_save_to_file_with_valid_list(self):
        # Test if save_to_file writes the correct JSON to the file
        input_list = [{"key1": "value1"}, {"key2": "value2"}]
        expected_result = '[{"key1": "value1"}, {"key2": "value2"}]'

        with unittest.mock.patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            YourClassName.save_to_file(input_list)

        mock_file().write.assert_called_once_with(expected_result)

class TestShapeDrawer(unittest.TestCase):

    def test_draw(self):

        list_rectangles = [Base(), Base()]
        list_squares = [Base(), Base()]  # 

        try:
            ShapeDrawer.draw(list_rectangles, list_squares)
        except Exception as e:
            self.fail(f"ShapeDrawer.draw raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()