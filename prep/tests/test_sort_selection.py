from typing import List

import numpy as np
import pytest

from prep import sort_selection

SIMPLE_UNSORTED = [5, 4, 3, 2, 1]
SIMPLE_SORTED = [1, 2, 3, 4, 5]
RANDOM_UNSORTED = list(np.random.randint(0, 100, 50))


@pytest.mark.parametrize(
    'nums',
    [SIMPLE_UNSORTED, SIMPLE_SORTED, RANDOM_UNSORTED],
    ids=['simple-unsorted', 'simple-sorted', 'random-unsorted'],
)
def test_selection_sort(nums: List[int]) -> None:
    # Setup - none necessary

    # Exercise
    result = sort_selection.selection_sort(nums)

    # Verify
    assert result == sorted(nums)

    # Cleanup - none necessary
