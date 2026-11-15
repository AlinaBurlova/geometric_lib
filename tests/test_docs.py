import unittest
import math
import circle, rectangle, square, triangle


class DocsTestCase(unittest.TestCase):
    """Проверка примеров из docstring/README."""

    def test_readme_circle_area(self):
        self.assertAlmostEqual(circle.area(10), 314.1592653589793, places=6)

    def test_readme_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(10), 62.83185307179586, places=6)

    def test_readme_rectangle(self):
        self.assertEqual(rectangle.area(5, 10), 50)
        self.assertEqual(rectangle.perimeter(5, 10), 30)

    def test_readme_square(self):
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.perimeter(10), 40)

    def test_readme_triangle(self):
        self.assertEqual(triangle.area(5, 10), 25.0)
        self.assertEqual(triangle.perimeter(5, 10, 15), 30)

    def test_all_functions_have_docstring(self):
        for mod in (circle, rectangle, square, triangle):
            for name in ("area", "perimeter"):
                self.assertIsNotNone(getattr(mod, name).__doc__)


if __name__ == "__main__":
    unittest.main()