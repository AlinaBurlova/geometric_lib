import unittest
import circle, rectangle, square, triangle


class IntegrationTestCase(unittest.TestCase):
    """Сквозные сценарии и согласованность модулей."""

    def test_all_modules_import(self):
        self.assertTrue(hasattr(circle, "area"))
        self.assertTrue(hasattr(rectangle, "area"))
        self.assertTrue(hasattr(square, "area"))
        self.assertTrue(hasattr(triangle, "area"))

    def test_determinism(self):
        self.assertEqual(circle.area(5), circle.area(5))
        self.assertEqual(triangle.perimeter(3, 4, 5), triangle.perimeter(3, 4, 5))

    def test_figure_full_cycle(self):
        self.assertEqual(rectangle.area(4, 5), 20)
        self.assertEqual(rectangle.perimeter(4, 5), 18)

    def test_composite_figure(self):
        s = square.area(4) + triangle.area(4, 3)
        self.assertEqual(s, 22.0)


if __name__ == "__main__":
    unittest.main()