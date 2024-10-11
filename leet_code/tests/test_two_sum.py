import unittest

from leet_code import two_sum


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.probs = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]

    def test_brute_force_solution(self):
        for nums, target, expected in self.probs:
            with self.subTest(nums=nums, target=target, expected=expected):
                result = two_sum.Solution().brute_solution(nums, target)
                self.assertEqual(sorted(result), sorted(expected))

    def test_other_solution(self):
        for nums, target, expected in self.probs:
            with self.subTest(nums=nums, target=target, expected=expected):
                result = two_sum.Solution().other_solution(nums, target)
                self.assertEqual(sorted(result), sorted(expected))

    def test_best_solution(self):
        for nums, target, expected in self.probs:
            with self.subTest(nums=nums, target=target, expected=expected):
                result = two_sum.Solution().twoSum(nums, target)
                self.assertEqual(sorted(result), sorted(expected))
