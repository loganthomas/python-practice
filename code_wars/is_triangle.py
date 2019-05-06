"""
Implement a method that accepts 3 integer values a, b, c.
The method should return true if a triangle can be built with the sides of given length and
false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""


def is_triangle(a, b, c):

    # Sort to ensure largest side last
    a, b, c = sorted([a, b, c])

    # triangle inequality theorem (with sorted)
    return a + b > c


if __name__ == '__main__':
    """ Simple tests. Consider refactoring with pytest later. """
    assert is_triangle(1, 2, 2)  is True , "fails when sides were 1, 2, 2"
    assert is_triangle(7, 2, 2)  is False, "fails when sides were 7, 2, 2"
    assert is_triangle(1, 2, 3)  is False, "fails when sides were 1, 2, 3"
    assert is_triangle(1, 3, 2)  is False, "fails when sides were 1, 3, 2"
    assert is_triangle(3, 1, 2)  is False, "fails when sides were 3, 1, 2"
    assert is_triangle(5, 1, 2)  is False, "fails when sides were 5, 1, 2"
    assert is_triangle(1, 2, 5)  is False, "fails when sides were 1, 2, 5"
    assert is_triangle(2, 5, 1)  is False, "fails when sides were 2, 5, 1"
    assert is_triangle(4, 2, 3)  is True , "fails when sides were 4, 2, 3"
    assert is_triangle(5, 1, 5)  is True , "fails when sides were 5, 1, 5"
    assert is_triangle(2, 2, 2)  is True , "fails when sides were 2, 2, 2"
    assert is_triangle(-1, 2, 3) is False, "fails when sides were -1, 2, 3"
    assert is_triangle(1, -2, 3) is False, "fails when sides were 1, -2, 3"
    assert is_triangle(1, 2, -3) is False, "fails when sides were 1, 2, -3"
    assert is_triangle(0, 2, 3)  is False, "fails when sides were 0, 2, 3"

    # Assuming asserts are never skipped/ignored
    print('Great Success!')

