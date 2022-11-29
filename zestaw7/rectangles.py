from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        out = '[' + str(self.pt1) + ', ' + str(self.pt2) + ']'
        return out

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        out = 'Rectangle(' + str(self.pt1.x) + ', ' + str(self.pt1.y) + ', ' + str(self.pt2.x) + ', ' + str(self.pt2.y) + ')'
        return out

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):            # pole powierzchni
        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)

    def intersection(self, other): # część wspólna prostokątów
        p1x = max(self.pt1.x, other.pt1.x)
        p1y = max(self.pt1.y, other.pt1.y)
        p2x = min(self.pt2.x, other.pt2.x)
        p2y = min(self.pt2.y, other.pt2.y)
        
        if(p1x > p2x or p1y > p2y):
            raise ValueError("Prostokąty nie mają części wspólnej")
        return Rectangle(p1x, p1y, p2x, p2y)

    def cover(self, other):    # prostąkąt nakrywający oba
        p1x = min(self.pt1.x, other.pt1.x)
        p1y = min(self.pt1.y, other.pt1.y)
        p2x = max(self.pt2.x, other.pt2.x)
        p2y = max(self.pt2.y, other.pt2.y)
        return Rectangle(p1x, p1y, p2x, p2y)

    def make4(self):           # zwraca krotkę czterech mniejszych
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C
        if(self == Rectangle()):
            raise ValueError("Brak prostokątu do podziału")
        return [Rectangle(self.pt1.x, self.pt1.y, (self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.x)/2),
				Rectangle((self.pt2.x + self.pt1.x)/2, self.pt1.y, self.pt2.x, (self.pt2.y + self.pt1.y)/2),
				Rectangle(self.pt1.x, (self.pt2.y + self.pt1.y)/2, (self.pt2.x + self.pt1.x)/2, self.pt2.y),
				Rectangle((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2, self.pt2.x, self.pt2.y)]

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
	def setUp(self):
		self.rect1 = Rectangle()
		self.rect2 = Rectangle(1, 2, 3, 4)
		self.rect3 = Rectangle(3, 4, 0, -2)
		self.rect4 = Rectangle(1, 2, 4, 5)
		self.rect5 = Rectangle(2, 1, 5, 4)
		self.rect6 = Rectangle(3, 1, 4, 2)
		self.rect7 = Rectangle(1, 1, 4, 4)
		self.rect8 = Rectangle(2, 2, 3, 3)


	def test_str(self):
		self.assertEqual(self.rect2.__str__(), "[(1, 2), (3, 4)]")	

	def test_repr(self):
		self.assertEqual(self.rect2.__repr__(), "Rectangle(1, 2, 3, 4)")

	def test_eq(self):
		self.assertEqual(self.rect2 == self.rect2, True)
		self.assertEqual(self.rect2 == self.rect1, False)

	def test_center(self):
		self.assertEqual(self.rect2.center(), Point(2, 3))

	def test_area(self):
		self.assertEqual(self.rect1.area(), 0)
		self.assertEqual(self.rect2.area(), 4)
		self.assertEqual(self.rect3.area(), 18)

	def test_move(self):
		self.rect1.move(2, 1)
		self.rect2.move(2, 1)
		self.assertEqual(self.rect1, Rectangle(2, 1, 2, 1))
		self.assertEqual(self.rect2, Rectangle(3, 3, 5, 5))

	def test_intersection(self):
		self.assertEqual(self.rect4.intersection(self.rect5), Rectangle(2, 2, 4, 4))
		with self.assertRaises(ValueError) as context:
			self.rect1.intersection(self.rect6)

	def test_cover(self):
		self.assertEqual(self.rect7.cover(self.rect8), self.rect7)
		self.assertEqual(self.rect4.cover(self.rect5), Rectangle(1, 1, 5, 5))

	def test_make4(self):
		self.assertEqual(self.rect7.make4(), [Rectangle(1, 1, 2.5, 2.5), 
			Rectangle(2.5, 1, 4, 2.5), Rectangle(1, 2.5, 2.5, 4), 
			Rectangle(2.5, 2.5, 4, 4)])
		with self.assertRaises(ValueError):
			self.rect1.make4()

if __name__ == '__main__':
	unittest.main()