"""
Count the number of occurrences of each character and return it as a list of tuples in order of
appearance.

Example:
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""
import pytest
from code_wars import count_of_chars


@pytest.mark.parametrize('_input,expected', [
    ['abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]],
    ['Code Wars'  , [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)]]
])
def test_ordered_count(_input, expected):
    # Setup
    expected = expected

    # Exercise
    result = count_of_chars.ordered_count(_input)

    # Verify
    assert result == expected

    # Cleanup - none necessary

