from typing import List
import pytest
from prep import fizzbuzz


@pytest.fixture
def expected_15() -> List[str]:
    return [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


def test_fizzbuzz_naive_n15(expected_15: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = fizzbuzz.fizzbuzz_naive(n=15)

    # Verify
    assert result == expected_15

    # Cleanup - none necessary


def test_fizzbuzz_concat_n15(expected_15: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = fizzbuzz.fizzbuzz_concat(n=15)

    # Verify
    assert result == expected_15

    # Cleanup - none necessary


def test_fizzbuzz_hash_n15(expected_15: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = fizzbuzz.fizzbuzz_hash(n=15)

    # Verify
    assert result == expected_15

    # Cleanup - none necessary


@pytest.fixture
def expected_30(expected_15: List[str]) -> List[str]:
    out = expected_15
    out.extend(
        [
            "16",
            "17",
            "Fizz",
            "19",
            "Buzz",
            "Fizz",
            "22",
            "23",
            "Fizz",
            "Buzz",
            "26",
            "Fizz",
            "28",
            "29",
            "FizzBuzz",
        ]
    )

    return out


def test_fizzbuzz_naive_n30(expected_30: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = fizzbuzz.fizzbuzz_naive(n=30)

    # Verify
    assert result == expected_30

    # Cleanup - none necessary


def test_fizzbuzz_concat_n30(expected_30: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = fizzbuzz.fizzbuzz_concat(n=30)

    # Verify
    assert result == expected_30

    # Cleanup - none necessary


def test_fizzbuzz_hash_n30(expected_30: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = fizzbuzz.fizzbuzz_hash(n=30)

    # Verify
    assert result == expected_30

    # Cleanup - none necessary
