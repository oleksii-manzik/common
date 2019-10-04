import unittest
import math

from .homework import Rectangle


class RectangleTestCase(unittest.TestCase):
    test_rectangle_1 = Rectangle(1, 4)
    test_rectangle_2 = Rectangle(10, 3)
    test_rectangle_3 = Rectangle(5, 5)

    def test_rectangle_perimeter_calc(self):
        self.assertEqual(self.test_rectangle_1.get_rectangle_perimeter(), 10)
        self.assertEqual(self.test_rectangle_2.get_rectangle_perimeter(), 26)
        self.assertEqual(self.test_rectangle_3.get_rectangle_perimeter(), 20)

    def test_rectangle_square_calc(self):
        self.assertEqual(self.test_rectangle_1.get_rectangle_square(), 4)
        self.assertEqual(self.test_rectangle_2.get_rectangle_square(), 30)
        self.assertEqual(self.test_rectangle_3.get_rectangle_square(), 25)

    def test_sum_of_corners_calc(self):
        for i in range(1, 5):
            with self.subTest(name=f'sum of {i} corners'):
                self.assertEqual(
                    self.test_rectangle_1.get_sum_of_corners(i), i * 90)

    def test_sum_of_corners_error_raise(self):
        for i in range(5, 10):
            with self.subTest(name=f'sum of {i} corners'):
                self.assertRaises(ValueError,
                                  self.test_rectangle_1.get_sum_of_corners, i)

    def test_rectangle_diagonal_calc(self):
        self.assertEqual(self.test_rectangle_1.get_rectangle_diagonal(),
                         math.sqrt(17))
        self.assertEqual(self.test_rectangle_2.get_rectangle_diagonal(),
                         math.sqrt(109))
        self.assertEqual(self.test_rectangle_3.get_rectangle_diagonal(),
                         math.sqrt(50))

    def test_radius_of_circumscribed_circle_calc(self):
        self.assertEqual(
            self.test_rectangle_1.get_radius_of_circumscribed_circle(),
            math.sqrt(17) / 2)
        self.assertEqual(
            self.test_rectangle_2.get_radius_of_circumscribed_circle(),
            math.sqrt(109) / 2)
        self.assertEqual(
            self.test_rectangle_3.get_radius_of_circumscribed_circle(),
            math.sqrt(50) / 2)

    def test_radius_of_inscribed_circle_calc(self):
        self.assertRaises(ValueError,
                          self.test_rectangle_1.get_radius_of_inscribed_circle)
        self.assertRaises(ValueError,
                          self.test_rectangle_2.get_radius_of_inscribed_circle)
        self.assertEqual(
            self.test_rectangle_3.get_radius_of_inscribed_circle(),
            math.sqrt(50) / (2 * math.sqrt(2)))


if __name__ == '__main__':
    unittest.main()
