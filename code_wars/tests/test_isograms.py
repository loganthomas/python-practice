"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""
import pytest
from code_wars import isograms


@pytest.mark.parametrize('string', ['Dermatoglyphics', "isogram", ""])
def test_isogram_for_true_isograms(string):
    # Setup
    expected = True

    # Exercise
    result = isograms.is_isogram(string)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('string', ["aba", "moOse", "isIsogram"])
def test_isogram_for_false_isograms(string):
    # Setup
    expected = False

    # Exercise
    result = isograms.is_isogram(string)

    # Verify
    assert result == expected

    # Cleanup - none necessary

