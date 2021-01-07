# Third-party libraries
import pytest

# Local libraries
from prep import chessboard


@pytest.mark.parametrize(
    "n, m, expected",
    [
        (3, 4, ".*.*\n*.*.\n.*.*\n"),
        (6, 8, ".*.*.*.*\n*.*.*.*.\n.*.*.*.*\n*.*.*.*.\n.*.*.*.*\n*.*.*.*.\n"),
        (8, 3, ".*.\n*.*\n.*.\n*.*\n.*.\n*.*\n.*.\n*.*\n"),
        (7, 5, ".*.*.\n*.*.*\n.*.*.\n*.*.*\n.*.*.\n*.*.*\n.*.*.\n"),
        (1, 6, ".*.*.*\n"),
        (8, 1, ".\n*\n.\n*\n.\n*\n.\n*\n"),
        (1, 1, ".\n"),
    ],
    ids=["3-3", "6-8", "8-3", "7-5", "1-6", "8-1", "1-1"],
)
def test_print_board(n: int, m: int, expected: str, capsys) -> None:
    # Setup

    # Exercise
    result = chessboard.print_board(n, m)
    captured = capsys.readouterr()

    # Verify
    assert result == expected
    assert captured.out[:-1] == expected

    # Cleanup - none necessary
