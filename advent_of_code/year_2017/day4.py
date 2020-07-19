"""
A new system policy has been put in place that requires all accounts to
use a passphrase instead of simply a password.

A passphrase consists of a series of words (lowercase letters) separated
by spaces. To ensure security, a valid passphrase must contain no
duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input.
How many passphrases are valid?

Puzzle:
day_4_puzzle.txt

Answer:
    Part 1 = 383
    Part 2 =
"""


def check_valid_passphrase(passphrase):
    """
    A passphrase consists of a series of words (lowercase letters)
    separated by spaces.
    """
    # Split passphrase on spaces
    splits = passphrase.split()

    # Valid if len of splits is the same as len of SET of splits (unique vals)
    return len(splits) == len(set(splits))


def count_valid_passphrases(data):
    """
    Check each passphrase within data and collect count of those valid.

    Args:
        data (list): List of strings

    Notes:
        - map() is slightly faster than list comprehension here.
    """
    return sum(map(check_valid_passphrase, data))

