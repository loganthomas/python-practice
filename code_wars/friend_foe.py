"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Ex: Input = ['Ryan', 'Kieran', 'Jason', 'Yous'], Output = ['Ryan', 'Yous']

Note: keep the original order of the names in the output.
"""


def friend(x):
    return [f for f in x if len(f) == 4]


if __name__ == '__main__':
    """ Simple tests. Consider refactoring with pytest later. """
    assert friend(['Ryan', 'Kieran', 'Mark',]) == ['Ryan', 'Mark'], "fails for ['Ryan', 'Kieran', 'Mark',])"
    assert friend(['Ry', 'K', 'M',]) == [], "fails for ['Ry', 'K', 'M',])"

    # Assuming asserts are never skipped/ignored
    print('Great Success!')

