from typing import List

import pytest

from prep import product_except_index


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 7, 3, 4], [84, 12, 28, 21]),
        ([1, 7, 3, 3], [63, 9, 21, 21]),
        ([1, 0, 0, 0], [0, 0, 0, 0]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
    ],
    ids=['[1, 7, 3, 4]', '[1, 7, 3, 3]', '[1, 0, 0, 0]', '[0, 0, 0, 0]'],
)
def test_find_products_with_division(nums: List[int], expected: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = product_except_index.find_products_with_division(nums)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 7, 3, 4], [84, 12, 28, 21]),
        ([1, 7, 3, 3], [63, 9, 21, 21]),
        ([1, 0, 0, 0], [0, 0, 0, 0]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
    ],
    ids=['[1, 7, 3, 4]', '[1, 7, 3, 3]', '[1, 0, 0, 0]', '[0, 0, 0, 0]'],
)
def test_find_products_without_division(nums: List[int], expected: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = product_except_index.find_products_without_division(nums)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 7, 3, 4], [84, 12, 28, 21]),
        ([1, 7, 3, 3], [63, 9, 21, 21]),
        ([1, 0, 0, 0], [0, 0, 0, 0]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
    ],
    ids=['[1, 7, 3, 4]', '[1, 7, 3, 3]', '[1, 0, 0, 0]', '[0, 0, 0, 0]'],
)
def test_find_products_optimized(nums: List[int], expected: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = product_except_index.find_products_optimized(nums)

    # Verify
    assert result == expected

    # Cleanup - none necessary
