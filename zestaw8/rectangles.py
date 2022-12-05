from points import Point

class Rectangle:
	"""Klasa reprezentujaca prostokaty na plaszczyznie."""

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

	def __eq__(self, other):   # obsluga rect1 == rect2
		return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

	def __ne__(self, other):        # obsluga rect1 != rect2
		return not self == other

	@property
	def center(self):          # zwraca srodek prostokata
		return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

	def area(self):            # pole powierzchni
		return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

	def move(self, x, y):      # przesuniecie o (x, y)
		self.pt1 = self.pt1 + Point(x, y)
		self.pt2 = self.pt2 + Point(x, y)

	def intersection(self, other): # czesc wspolna prostokatow
		p1x = max(self.pt1.x, other.pt1.x)
		p1y = max(self.pt1.y, other.pt1.y)
		p2x = min(self.pt2.x, other.pt2.x)
		p2y = min(self.pt2.y, other.pt2.y)
		
		if(p1x > p2x or p1y > p2y):
			raise ValueError("Prostokaty nie maja czesci wspolnej")
		return Rectangle(p1x, p1y, p2x, p2y)

	def cover(self, other):    # prostakat nakrywajacy oba
		p1x = min(self.pt1.x, other.pt1.x)
		p1y = min(self.pt1.y, other.pt1.y)
		p2x = max(self.pt2.x, other.pt2.x)
		p2y = max(self.pt2.y, other.pt2.y)
		return Rectangle(p1x, p1y, p2x, p2y)

	def make4(self):           # zwraca krotke czterech mniejszych
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C
		if(self == Rectangle()):
			raise ValueError("Brak prostokatu do podzialu")
		return [Rectangle(self.pt1.x, self.pt1.y, (self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.x)/2),
				Rectangle((self.pt2.x + self.pt1.x)/2, self.pt1.y, self.pt2.x, (self.pt2.y + self.pt1.y)/2),
				Rectangle(self.pt1.x, (self.pt2.y + self.pt1.y)/2, (self.pt2.x + self.pt1.x)/2, self.pt2.y),
				Rectangle((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2, self.pt2.x, self.pt2.y)]

	@classmethod
	def from_points(cls, points):
		point1, point2 = points
		return cls(point1.x, point1.y, point2.x, point2.y)

	@property
	def top(self):
		return self.pt2.y

	@property
	def bottom(self):
		return self.pt1.y

	@property
	def left(self):
		return self.pt1.x

	@property
	def right(self):
		return self.pt2.x
	
	@property
	def width(self):
		wid = self.pt2.x - self.pt1.x
		return wid

	@property
	def height(self):
		hei = self.pt2.y - self.pt1.y
		return hei
	
	@property
	def topleft(self):
		return Point(self.pt1.x, self.pt2.y)

	@property
	def bottomleft(self):
		return Point(self.pt1.x, self.pt1.y)
		
	@property
	def topright(self):
		return Point(self.pt2.x, self.pt2.y)
		
	@property
	def bottomright(self):
		return Point(self.pt2.x, self.pt1.y)