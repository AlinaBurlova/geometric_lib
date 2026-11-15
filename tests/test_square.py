import unittest
from square import area, perimeter
from rectangle import area as rect_area, perimeter as rect_perimeter


class SquareTestCase(unittest.TestCase):
    """Unit-тесты для square.py."""

    def test_area_positive(self):
        self.assertEqual(area(10), 100)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(10), 40)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_negative_current_behavior(self):
        self.assertEqual(area(-5), 25)

    def test_area_matches_rectangle(self):
        self.assertEqual(area(7), rect_area(7, 7))

    def test_perimeter_matches_rectangle(self):
        self.assertEqual(perimeter(7), rect_perimeter(7, 7))


if __name__ == "__main__":
    unittest.main()