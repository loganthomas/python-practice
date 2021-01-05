import pytest

from prep import skyline


def test_gather_skyline() -> None:
    # Setup
    buildings = [[2, 9, 10], [5, 12, 12], [3, 7, 15], [19, 24, 8], [15, 20, 10]]
    expected = [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]

    # Exercise
    result = skyline.gather_skyline_keypoints(buildings)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.mpl_image_compare()
def test_plot_skyline() -> None:
    """
    Notes:
    - Run via `pytest --mpl`
    - Remove text when using pytest-mpl with:
      @pytest.mark.mpl_image_compare(remove_text=True).
      This will remove (titles, axes, labels, etc.)
    - First run needs to specify where to store base image for
      comparison later on:
      pytest -k skyline --mpl-generate-path=prep/tests/baseline
    - Above must have "baseline" as directory
    """
    # Setup
    buildings = [[2, 9, 10], [5, 12, 12], [3, 7, 15], [19, 24, 8], [15, 20, 10]]

    # Exercise
    fig = skyline.plot_skyline(buildings)

    # Verify - none necessary (handled by pytest-mpl)

    # Clean up - none necessary

    # Required for pytest-mpl for image testing
    return fig


@pytest.mark.mpl_image_compare()
def test_plot_skyline_with_keypoints() -> None:
    """
    Notes:
    - Run via `pytest --mpl`
    - Remove text when using pytest-mpl with:
      @pytest.mark.mpl_image_compare(remove_text=True).
      This will remove (titles, axes, labels, etc.)
    - First run needs to specify where to store base image for
      comparison later on:
      pytest -k skyline --mpl-generate-path=prep/tests/baseline
    - Above must have "baseline" as directory
    """
    # Setup
    buildings = [[2, 9, 10], [5, 12, 12], [3, 7, 15], [19, 24, 8], [15, 20, 10]]
    expected = [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8), (24, 0)]

    # Exercise
    keypoints = skyline.gather_skyline_keypoints(buildings)
    fig = skyline.plot_skyline_with_keypoints(buildings, keypoints)

    # Verify
    assert keypoints == expected

    # Clean up - none necessary

    # Required for pytest-mpl for image testing
    return fig
