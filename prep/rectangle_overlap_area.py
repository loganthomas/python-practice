"""
Problem 2: Area of Rectangles Overlap
-------------------------------------

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2],
where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2)
is the coordinate of its top-right corner.

Its top and bottom edges are parallel to the X-axis, and its left and
right edges are parallel to the Y-axis.

Given two axis-aligned rectangles rec1 and rec2, return the area of the
resulting overlap rectangle. If the rectangles do not overlap,
return false.


Example 1:
----------
Input: rec1 = [2, 2, 5, 7], rec2 = [3, 4, 6, 9]
Output: 6

Example 2:
----------
Input: rec1 = [2, 1, 5, 5], rec2 = [3, 2, 5, 7]
Output: 6

Example 3:
----------
Input: rec1 = [0, 0, 1, 1], rec2 = [1, 0, 2, 1]
Output: false

Example 4:
----------
Input: rec1 = [3, 3, 5, 5], rec2 = [1, 1, 4, 3.5]
Output: 0.5
"""

# Standard libraries
from collections import namedtuple
from typing import Union

Rect = namedtuple('Rect', ('bl_x', 'bl_y', 'tr_x', 'tr_y'))


def calc_overlap_area(rect1: Rect, rect2: Rect) -> Union[bool, int]:
    width = min(rect1.tr_x, rect2.tr_x) - max(rect1.bl_x, rect2.bl_x)
    length = min(rect1.tr_y, rect2.tr_y) - max(rect1.bl_y, rect2.bl_y)

    if (width <= 0) or (length <= 0):
        return False

    return width * length
