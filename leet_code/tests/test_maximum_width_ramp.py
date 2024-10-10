# Standard libraries
import unittest

# Local libraries
from leet_code import maximum_width_ramp


class TestMaximumWidthRamp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = [
            (
                [
                    29,
                    28,
                    26,
                    25,
                    9,
                    25,
                    28,
                    22,
                    20,
                    20,
                    19,
                    19,
                    17,
                    17,
                    16,
                    29,
                    15,
                    15,
                    15,
                    13,
                    5,
                    10,
                    10,
                    9,
                    28,
                    6,
                    0,
                    3,
                    0,
                    0,
                ],
                23,
            ),
            ([6, 0, 8, 2, 1, 5], 4),
            ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7),
            ([2, 2, 1], 1),
            ([0, 1], 1),
            ([1, 0], 0),
        ]

    def test_Solution1(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = maximum_width_ramp.Solution1().maxWidthRamp(nums)
                self.assertEqual(result, expected)

    def test_Solution2(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = maximum_width_ramp.Solution2().maxWidthRamp(nums)
                self.assertEqual(result, expected)

    def test_Solution3(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = maximum_width_ramp.Solution3().maxWidthRamp(nums)
                self.assertEqual(result, expected)

    def test_SolutionA(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = maximum_width_ramp.SolutionA().maxWidthRamp(nums)
                self.assertEqual(result, expected)

    def test_SolutionB(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = maximum_width_ramp.SolutionB().maxWidthRamp(nums)
                self.assertEqual(result, expected)

    def test_SolutionC(self):
        for nums, expected in self.cases:
            with self.subTest(nums=nums, expected=expected):
                result = maximum_width_ramp.SolutionC().maxWidthRamp(nums)
                self.assertEqual(result, expected)
