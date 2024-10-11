from pathlib import Path

import pytest

from advent_of_code.year_2017 import day4


@pytest.mark.parametrize(
    'passphrase, expected',
    [
        ('aa bb cc dd ee', True),
        ('aa bb cc dd aa', False),
        ('aa bb cc dd aaa', True),
    ],
    ids=['provided-valid1', 'provided-invalid', 'provided-valid2'],
)
def test_check_valid_passphrase(passphrase, expected):
    # Setup - none necessary

    # Exercise
    result = day4.check_valid_passphrase(passphrase)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'data, expected',
    [
        (['aa', 'bb', 'cc'], 3),
        (['aa aa', 'bb bb', 'cc cc'], 0),
        (['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa'], 2),
    ],
    ids=['simple-all-valid', 'simple-none-valid', 'simple-provided'],
)
def test_count_valid_passphrases(data, expected):
    # Setup - none necessary

    # Exercise
    result = day4.count_valid_passphrases(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_day4_part1_answer():
    # Setup
    data_path = Path('advent_of_code/year_2017/data/day4_puzzle.txt')
    expected = 383

    with open(data_path) as f:
        data = f.readlines()
        data = [row.strip() for row in data]

    # Exercise
    result = day4.count_valid_passphrases(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary
