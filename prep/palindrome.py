"""
Palindrome
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


def is_palindrome_index(s: str) -> bool:
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
