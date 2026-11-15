import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    """Unit-тесты для triangle.py."""

    def test_area_positive(self):
        self.assertEqual(area(5, 10), 25.0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5, 10, 15), 30)

    def test_area_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_area_returns_float(self):
        self.assertIsInstance(area(5, 10), float)

    def test_perimeter_wrong_arity(self):
        with self.assertRaises(TypeError):
            perimeter(5, 10)

    def test_perimeter_invalid_triangle_current_behavior(self):
        self.assertEqual(perimeter(1, 1, 100), 102)


if __name__ == "__main__":
    unittest.main()