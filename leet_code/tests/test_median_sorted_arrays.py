import unittest
from leet_code import median_sorted_arrays


class TestMedianSortedArrays(unittest.TestCase):
    def setUp(self):
        self.probs = [
            ([1, 3], [2], 2),
            ([1, 2], [3, 4], 2.5),
        ]

    def test_solution(self):
        for nums1, nums2, expected in self.probs:
            with self.subTest(nums1=nums1, nums2=nums2, expected=expected):
                result = median_sorted_arrays.Solution().findMedianSortedArrays(
                    nums1, nums2
                )
                self.assertEqual(result, expected)
