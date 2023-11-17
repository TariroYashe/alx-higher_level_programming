
#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 20, 30, 40, 50)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 20, 30, 40, 50)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "invalid", 30, 40, 50)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0, 30, 40, 50)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "invalid", 40, 50)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5, 40, 50)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 30, "invalid", 50)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 30, -5, 50)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(60, 5, 15, 25, 35)
        self.assertEqual(r.id, 60)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 25)
        self.assertEqual(r.y, 35)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 30, 40, 50)
        expected_dict = {
            "id": 50,
            "width": 10,
            "height": 20,
            "x": 30,
            "y": 40
        }
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_str_representation(self):
        r = Rectangle(10, 20, 30, 40, 50)
        expected_str = "[Rectangle] (50) 30/40 - 10/20"
        self.assertEqual(str(r), expected_str)


if __name__ == "__main__":
    unittest.main()
