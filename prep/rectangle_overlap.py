"""
Problem 1: Overlapping Rectangles
---------------------------------

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2],
where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2)
is the coordinate of its top-right corner.

Its top and bottom edges are parallel to the X-axis, and its left and
right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive.
To be clear, two rectangles that only touch at the corner or edges
DO NOT overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they
overlap, otherwise return false.


Example 1:
----------
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:
----------
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Example 3:
----------
Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
"""

from collections import namedtuple

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

Rect = namedtuple('Rect', ('bl_x', 'bl_y', 'tr_x', 'tr_y'))


def is_overlap(rect1: Rect, rect2: Rect) -> bool:
    # Think min of rect1 and max of rect2
    if (rect1.bl_x >= rect2.tr_x) or (rect1.bl_y >= rect2.tr_y):
        return False

    # Think max of rect1 and min of rect2
    if (rect1.tr_x <= rect2.bl_x) or (rect1.tr_y <= rect2.bl_y):
        return False

    return True


def plot_rects(rect1: Rect, rect2: Rect) -> plt.Figure:
    fig = plt.figure()

    ax = fig.add_subplot()  # nrows=1, ncols=1, index=1

    ax.add_patch(
        Rectangle(
            xy=(rect1.bl_x, rect1.bl_y),
            width=rect1.tr_x - rect1.bl_x,
            height=rect1.tr_y - rect1.bl_y,
            edgecolor='blue',
            fill=False,
        )
    )

    ax.add_patch(
        Rectangle(
            xy=(rect2.bl_x, rect2.bl_y),
            width=rect2.tr_x - rect2.bl_x,
            height=rect2.tr_y - rect2.bl_y,
            edgecolor='orange',
            fill=False,
        )
    )

    plt.xlim([min(rect1.bl_x, rect2.bl_x) - 1, max(rect1.tr_x, rect2.tr_x) + 1])
    plt.ylim([min(rect1.bl_y, rect2.bl_y) - 1, max(rect1.tr_y, rect2.tr_y) + 1])

    overlap = is_overlap(rect1, rect2)
    plt.title(f'Rectangle Overlap: {overlap}')

    return fig
