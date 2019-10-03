"""
Count the number of occurrences of each character and return it as a list of tuples in order of
appearance.

Example:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""
from collections import Counter


def ordered_count(_input):
    return list(Counter(_input).items())


if __name__ == '__main__':
    """ Simple tests. Consider refactoring with pytest later. """
    assert ordered_count('abracadabra') == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)], (
        "fails for 'abracadabra'")
    assert ordered_count('Code Wars') == [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)], (
        "fails for 'Code Wars'")

    # Assuming asserts are never skipped/ignored
    print('Great Success!')

