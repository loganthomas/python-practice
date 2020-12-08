"""
Check Palindrome
----------

A string of letters is a palindrome if it is identical to it's reversion.

Write a function that checks whether or not a provided string is a
palindrome.


Notes
-----
s = "ablewasiereisawelba"
%timeit palindrome.is_palindrome_index(s)
203 ns ± 1.26 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit palindrome.is_palindrome_ij(s)
1.12 µs ± 2.32 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit palindrome.is_palindrome_mid(s)
1.36 µs ± 2.83 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
"""
from typing import List


def is_palindrome_slicing(s: str) -> bool:
    """ Using string indexing. """
    return s == s[::-1]


def is_palindrome_ij(s: str) -> bool:
    """ Using an i and j index. """
    i = 0
    j = len(s) - 1

    while j > i:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


def is_palindrome_mid(s: str) -> bool:
    """ Using a midpoint. """
    m = len(s) // 2

    for i in range(m):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# Generate Palindrome
# -------------------
# Now, write a function that will generate a palindrome given a base string.
# Use the function you created above to check your new function

# Notes
# -----
# s = "aaaaaabbbbbcccccdddddeeeee"

# %timeit palindrome.generate_palindrome_slicing(s)
# 296 ns ± 1.25 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit palindrome.generate_palindrome_list(s)
# 3.4 µs ± 34.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# %timeit palindrome.generate_palindrome_build(s)
# 2.69 µs ± 10.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


def generate_palindrome_slicing(s: str) -> str:
    return "".join([s, s[::-1]])


def generate_palindrome_list(s: str) -> str:
    out: List[str] = [""] * len(s) * 2

    for i, x in enumerate(s):
        out[i] = x
        out[-(i + 1)] = x

    return "".join(out)


def generate_palindrome_build(s: str) -> str:
    j = len(s) - 1

    while j >= 0:
        s += s[j]
        j -= 1
    return s
