"""
Check Anagram
-------------

A word, phrase, or name formed by rearranging the letters of another
is called an anagram. For example, cinema is an anagram of iceman.

Write a function that checks whether or two provided strings are anagrams.


Notes
-----
string_pairs = ("eleven plus two", "twelve plus one")

%timeit anagram.is_anagram_sort(*string_pairs)
1.13 µs ± 5.86 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit anagram.is_anagram_count(*string_pairs)
4.76 µs ± 105 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
"""

from collections import Counter


def is_anagram_sort(string_1: str, string_2: str) -> bool:
    return sorted(string_1) == sorted(string_2)


def is_anagram_count(string_1: str, string_2: str) -> bool:
    return Counter(string_1) == Counter(string_2)
