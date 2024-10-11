# Standard libraries
import unittest

# Local libraries
from leet_code import smallest_unoccupied_chair


class TestSmallestUnoccupiedChair(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Examples cases of form times, target, expected.
        """
        cls.cases = [
            ([[1, 4], [2, 3], [4, 6]], 1, 1),
            ([[3, 10], [1, 5], [2, 6]], 0, 2),
            (
                [
                    [33889, 98676],
                    [80071, 89737],
                    [44118, 52565],
                    [52992, 84310],
                    [78492, 88209],
                    [21695, 67063],
                    [84622, 95452],
                    [98048, 98856],
                    [98411, 99433],
                    [55333, 56548],
                    [65375, 88566],
                    [55011, 62821],
                    [48548, 48656],
                    [87396, 94825],
                    [55273, 81868],
                    [75629, 91467],
                ],
                6,
                2,
            ),
        ]

    def test_smallest_chair(self):
        for times, target, expected in self.cases:
            with self.subTest(times=times, target=target, expected=expected):
                result = smallest_unoccupied_chair.smallest_chair(times, target)
                self.assertEqual(result, expected)

    def test_smallest_chair2(self):
        for times, target, expected in self.cases:
            with self.subTest(times=times, target=target, expected=expected):
                result = smallest_unoccupied_chair.smallest_chair2(times, target)
                self.assertEqual(result, expected)
