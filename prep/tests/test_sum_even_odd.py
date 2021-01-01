from prep import sum_even_odd
import pytest


@pytest.mark.parametrize(
    "n, expected_even_sum, expected_odd_sum",
    [(5, 6, 4), (7, 12, 9), (10, 20, 25), (15, 56, 49)],
    ids=["n-5", "n-7", "n-10", "n-15"],
)
def test_sum_even_odd_slicing(
    n: int, expected_even_sum: int, expected_odd_sum: int
) -> None:
    # Setup - none necessary

    # Exercise
    result_even_sum, result_odd_sum = sum_even_odd.sum_even_odd_slicing(n)

    # Verify
    assert result_even_sum == expected_even_sum
    assert result_odd_sum == expected_odd_sum

    # Cleanup - none necessary


@pytest.mark.parametrize(
    "n, expected_even_sum, expected_odd_sum",
    [(5, 6, 4), (7, 12, 9), (10, 20, 25), (15, 56, 49)],
    ids=["n-5", "n-7", "n-10", "n-15"],
)
def test_sum_even_odd_mod(
    n: int, expected_even_sum: int, expected_odd_sum: int
) -> None:
    # Setup - none necessary

    # Exercise
    result_even_sum, result_odd_sum = sum_even_odd.sum_even_odd_mod(n)

    # Verify
    assert result_even_sum == expected_even_sum
    assert result_odd_sum == expected_odd_sum

    # Cleanup - none necessary
