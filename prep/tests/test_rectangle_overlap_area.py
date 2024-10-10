# Third-party libraries
import pytest
from typing import List, Union

# Local libraries
from prep import rectangle_overlap_area


@pytest.mark.parametrize(
    "rec1, rec2, expected",
    (
        [[2, 2, 5, 7], [3, 4, 6, 9], 6],  # overlap-area1
        [[2, 1, 5, 5], [3, 2, 5, 7], 6],  # overlap-area2
        [[3, 3, 5, 5], [1, 1, 4, 3.5], 0.5],  # overlap-area3
        [[0, 0, 1, 1], [1, 0, 2, 1], False],  # false-no-overlap1
        [[0, 0, 1, 1], [2, 2, 3, 3], False],  # false-no-overlap2
        [[2, 2, 3, 3], [0, 0, 1, 1], False],  # false-no-overlap3
    ),
    ids=[
        "overlap-area1",
        "overlap-area2",
        "overlap-area3",
        "false-no-overlap1",
        "false-no-overlap2",
        "false-no-overlap3",
    ],
)
def test_calc_overlap_area(
    rec1: List, rec2: List, expected: Union[float, int, bool]
) -> None:
    # Setup
    rect1 = rectangle_overlap_area.Rect(*rec1)
    rect2 = rectangle_overlap_area.Rect(*rec2)

    # Exercise
    result = rectangle_overlap_area.calc_overlap_area(rect1, rect2)

    # Verify
    assert result == expected

    # Cleanup - none necessary
