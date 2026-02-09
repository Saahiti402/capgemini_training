import unittest
from math import pi

class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r * self.r


class TestShapeArea(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(Rectangle(4, 5).area(), 20)

    def test_circle_area(self):
        self.assertAlmostEqual(Circle(7).area(), pi * 49)


if __name__ == "__main__":
    unittest.main()