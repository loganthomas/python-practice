"""
Simple Chessboard
----------------
Given two numbers, n and m, create a two-dimensional array of size
(n X m) and populate it with the characters "." and "*" in a
checkerboard pattern. The top left corner should have the character "."

Example 1:
----------
n=3 m=4
. * . *
* . * .
. * . *

Example 2:
----------
n=6 m=8
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .

Example 3:
----------
n=8 m=3
. * .
* . *
. * .
* . *
. * .
* . *
. * .
* . *

Example 4:
----------
n=7 m=5
. * . * .
* . * . *
. * . * .
* . * . *
. * . * .
* . * . *
. * . * .

Example 5:
----------
n=1 m=6
. * . * . *

Example 6:
----------
n=8 m=2
.
*
.
*
.
*
.
*

Example 7:
----------
n=1 m=1
.
"""


def print_board(n: int, m: int, verbose: bool = True) -> str:
    out = ""
    for i in range(n):
        row = ""
        for j in range(m):
            if (i + j) % 2 == 0:
                row += "."
            else:
                row += "*"
        out += row + "\n"

    if verbose:
        print(out)

    return out
