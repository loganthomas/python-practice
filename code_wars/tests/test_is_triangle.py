"""
Implement a method that accepts 3 integer values a, b, c.
The method should return true if a triangle can be built with the sides of given length and
false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""

import math
import random

import pytest

from code_wars import is_triangle

true_tris = [(1, 2, 2), (4, 2, 3), (5, 1, 5), (2, 2, 2)]
false_tris = [
    (7, 2, 2),
    (1, 2, 3),
    (1, 3, 2),
    (3, 1, 2),
    (5, 1, 2),
    (1, 2, 5),
    (2, 5, 1),
    (-1, 2, 3),
    (1, -2, 3),
    (1, 2, -3),
    (0, 2, 3),
]


# Can parametrize rather than writing multiple test functions for same thing!
#     I would have had to write a different function for each true_tri that did the same thing...
@pytest.mark.parametrize('a,b,c', true_tris)
def test_true_triangle(a, b, c):
    """
    Test if is_triangle returns true for valid triangle.
    """
    # Setup
    expected = True

    # Exercise
    result = is_triangle.is_triangle(a, b, c)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('a,b,c', false_tris)
def test_false_triangle(a, b, c):
    """
    Test if is_triangle returns true for valid triangle.
    """
    # Setup
    expected = False

    # Exercise
    result = is_triangle.is_triangle(a, b, c)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'a,b', [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(5)]
)
def test_random_true_triangle(a, b):
    # Setup
    c = math.sqrt(a**2 + b**2)
    expected = True

    # Exercise
    result = is_triangle.is_triangle(a, b, c)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'x,y', [(random.randint(1, 500), random.randint(1, 2500)) for _ in range(5)]
)
def test_random_false_triangle(x, y):
    # Setup
    z = x + y + 1
    expected = False

    # Exercise
    result = is_triangle.is_triangle(x, y, z)

    # Verify
    assert result == expected

    # Cleanup - none necessary
