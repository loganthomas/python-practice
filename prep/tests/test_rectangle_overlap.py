import ast
from typing import List

import pytest

from prep import rectangle_overlap


@pytest.mark.parametrize(
    'rec1, rec2, expected',
    (
        [[0, 0, 2, 2], [1, 1, 3, 3], True],  # true-overlap1
        [[0, 0, 1, 1], [1, 0, 2, 1], False],  # false-overlap-touching
        [[0, 0, 1, 1], [2, 2, 3, 3], False],  # false-no-overlap1
        [[2, 2, 3, 3], [0, 0, 1, 1], False],  # false-no-overlap2
        [[0, 0, 10, 10], [5, 0, 15, 5], True],  # true-overlap2
        [[5, 0, 15, 5], [0, 0, 10, 10], True],  # true-overlap3
    ),
    ids=[
        'true-overlap1',
        'false-overlap-touching',
        'false-no-overlap1',
        'false-no-overlap2',
        'true-overlap2',
        'true-overlap3',
    ],
)
def test_is_overlap(rec1: List, rec2: List, expected: bool) -> None:
    # Setup
    rect1 = rectangle_overlap.Rect(*rec1)
    rect2 = rectangle_overlap.Rect(*rec2)

    # Exercise
    result = rectangle_overlap.is_overlap(rect1, rect2)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'rec1, rec2, expected',
    (
        [[0, 0, 2, 2], [1, 1, 3, 3], True],  # true-overlap1
        [[0, 0, 1, 1], [1, 0, 2, 1], False],  # false-overlap-touching
        [[0, 0, 1, 1], [2, 2, 3, 3], False],  # false-no-overlap1
        [[2, 2, 3, 3], [0, 0, 1, 1], False],  # false-no-overlap2
        [[0, 0, 10, 10], [5, 0, 15, 5], True],  # true-overlap2
        [[5, 0, 15, 5], [0, 0, 10, 10], True],  # true-overlap3
    ),
    ids=[
        'true-overlap1',
        'false-overlap-touching',
        'false-no-overlap1',
        'false-no-overlap2',
        'true-overlap2',
        'true-overlap3',
    ],
)
@pytest.mark.mpl_image_compare()
def test_plot_rects(rec1: List, rec2: List, expected: bool) -> None:
    """
    Notes:
        - Run via `pytest --mpl`
        - Remove text when using pytest-mpl with:
          @pytest.mark.mpl_image_compare(remove_text=True).
          This will remove (titles, axes, labels, etc.)
        - First run needs to specify where to store base image for
          comparison later on:
          pytest -k test_plot_rects --mpl-generate-path=prep/tests/baseline
        - Above must have "baseline" as directory
    """
    # Setup
    rect1 = rectangle_overlap.Rect(*rec1)
    rect2 = rectangle_overlap.Rect(*rec2)

    # Exercise
    fig = rectangle_overlap.plot_rects(rect1, rect2)
    result = ast.literal_eval(fig.axes[0].get_title().replace('Rectangle Overlap: ', ''))

    # Verify
    assert result == expected

    # Cleanup - none necessary

    # Required for pytest-mpl for image testing
    return fig
