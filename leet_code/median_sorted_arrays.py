"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List


def update_slices(larger_side, smaller_side, larger_idx, smaller_idx, tgt):
    lb, ub = larger_idx + smaller_idx + 1, larger_idx + smaller_idx
    larger_side[1] = max(min(larger_side[1], larger_idx + 1 + tgt - lb), larger_idx)
    smaller_side[0] = min(max(0, smaller_idx + tgt - ub), smaller_idx + 1)


def select(left, right, left_slice, right_slice, tgt):
    n, m = left_slice[1] - left_slice[0], right_slice[1] - right_slice[0]
    if n == 0:
        idx = tgt - left_slice[0]
        return right[idx], (None, idx)
    if m == 0:
        idx = tgt - right_slice[0]
        return left[idx], (idx, None)

    i, j = n // 2 + left_slice[0], m // 2 + right_slice[0]
    val_l, val_r = left[i], right[j]
    if val_l >= val_r:
        update_slices(left_slice, right_slice, i, j, tgt)
    else:
        update_slices(right_slice, left_slice, j, i, tgt)

    return select(left, right, left_slice, right_slice, tgt)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        N = n + m
        tgt = N // 2
        if N % 2 == 0:
            a, (i, j) = select(nums1, nums2, [0, n], [0, m], tgt)
            if i is not None:
                b, _ = select(nums1, nums2, [max(0, i - 1), i], [0, m], tgt - 1)
            else:
                b, _ = select(nums1, nums2, [0, n], [max(0, j - 1), j], tgt - 1)
            out = (a + b) / 2
        else:
            out, _ = select(nums1, nums2, [0, n], [0, m], tgt)
        return out
