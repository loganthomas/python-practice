import unittest

from leet_code import smallest_range_covering_elements


class TestSmallestRangeCoveringElements(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = [
            ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
            ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 1]),
            ([[10, 10], [11, 11]], [10, 11]),
            ([[1], [2], [3], [4], [5], [6], [7]], [1, 7]),
            ([[-5, -4, -3, -2, -1, 1], [1, 2, 3, 4, 5]], [1, 1]),
        ]

    def test_smallest_range(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = smallest_range_covering_elements.smallest_range(nums)
                self.assertEqual(result, expected)

    def test_smallest_range2(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = smallest_range_covering_elements.smallest_range2(nums)
                self.assertEqual(result, expected)
