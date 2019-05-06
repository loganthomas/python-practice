"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""


def is_isogram(string):
    # Ensure all same case
    s = string.lower()

    # Use set for distinct chars within string
    return len(s) == len(set(s))


if __name__ == '__main__':
    """ Simple tests. Consider refactoring with pytest later. """
    assert is_isogram("Dermatoglyphics") is True, "fails for Dermatoglyphics"
    assert is_isogram("isogram")         is True, "fails for isogram"
    assert is_isogram("aba")             is False, "fails for aba"
    assert is_isogram("moOse")           is False, "fails for moOse"
    assert is_isogram("isIsogram")       is False, "fails for isIsogram"
    assert is_isogram("")                is True , "fails for empty string"
    # Assuming asserts are never skipped/ignored
    print('Great Success!')

