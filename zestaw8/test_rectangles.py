from points import Point
from rectangles import Rectangle

def test_from_points():
    rectangle = Rectangle.from_points((Point(1, 1), Point(3, 4)))
    assert str(rectangle) == '[(1, 1), (3, 4)]'


def test_coords_getters():
    rect = Rectangle(1, 1, 4, 4)

    assert rect.top == 4
    assert rect.bottom == 1

    assert rect.left == 1
    assert rect.right == 4

    assert rect.height == 3
    assert rect.width == 3


def test_point_getters():
    p1 = Point(0, 1)
    p2 = Point(3, 4)
    rect = Rectangle.from_points((p1, p2))

    assert rect.bottomleft == p1
    assert rect.topright == p2
    assert rect.topleft == Point(p1.x, p2.y)
    assert rect.bottomright == Point(p2.x, p1.y)


def test_center():
    assert Rectangle(0, 1, 3, 4).center == Point(1, 2)