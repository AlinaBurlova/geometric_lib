import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    """Unit-тесты для circle.py."""

    def test_area_positive(self):
        self.assertAlmostEqual(area(10), math.pi * 100, places=9)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), math.pi, places=9)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(10), 2 * math.pi * 10, places=9)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_small(self):
        self.assertAlmostEqual(area(1e-9), math.pi * 1e-18, places=20)

    def test_area_large(self):
        self.assertAlmostEqual(area(1e9), math.pi * 1e18, delta=1e9)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_string_raises(self):
        with self.assertRaises(TypeError):
            area("10")

    def test_area_none_raises(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_area_returns_float(self):
        self.assertIsInstance(area(10), float)


if __name__ == "__main__":
    unittest.main()