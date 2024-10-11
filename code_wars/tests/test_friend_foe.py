"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Ex: Input = ['Ryan', 'Kieran', 'Jason', 'Yous'], Output = ['Ryan', 'Yous']

Note: keep the original order of the names in the output.
"""

from code_wars import friend_foe


def test_friend_4_ins():
    """
    Test if friend returns correct values.
    """
    # Setup
    people = ['Ryan', 'Kieran', 'Jason', 'Yous']
    friends = ['Ryan', 'Yous']

    # Exercise
    result = friend_foe.friend(people)

    # Verify
    assert result == friends

    # Cleanup - none necessary


def test_friend_3_ins():
    """
    Test if friend returns correct values.
    """
    # Setup
    people = ['Ryan', 'Kieran', 'Mark']
    friends = ['Ryan', 'Mark']

    # Exercise
    result = friend_foe.friend(people)

    # Verify
    assert result == friends

    # Cleanup - none necessary


def test_friend_1_ins():
    """
    Test if friend returns correct values.
    """
    # Setup
    people = ['Loge']
    friends = ['Loge']

    # Exercise
    result = friend_foe.friend(people)

    # Verify
    assert result == friends

    # Cleanup - none necessary


def test_friend_none():
    """
    Test if friend returns no values.
    """
    # Setup
    people = ['Ry', 'K', 'M']
    friends = []

    # Exercise
    result = friend_foe.friend(people)

    # Verify
    assert result == friends

    # Cleanup - none necessary
