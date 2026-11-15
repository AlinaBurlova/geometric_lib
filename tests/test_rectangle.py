import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    """Unit-тесты для rectangle.py."""

    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_positive(self):
        self.assertEqual(area(5, 10), 50)

    def test_perimeter_basic(self):
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_area_string_current_behavior(self):
        self.assertEqual(area("5", 10), "5555555555")

    def test_area_two_strings_raises(self):
        with self.assertRaises(TypeError):
            area("5", "10")

    def test_perimeter_regression_fix(self):
        self.assertEqual(perimeter(5, 10), 30)
        self.assertNotEqual(perimeter(5, 10), 15)

    def test_perimeter_square_case(self):
        self.assertEqual(perimeter(10, 10), 40)


if __name__ == "__main__":
    unittest.main()