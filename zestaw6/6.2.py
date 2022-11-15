import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        out = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return out

    def __repr__(self):        # zwraca string "Point(x, y)"
        out = 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
        return out

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        x_out = self.x + other.x
        y_out = self.y + other.y
        return Point.__init__(self,x_out, y_out)

    def __sub__(self, other): pass  # v1 - v2

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): pass