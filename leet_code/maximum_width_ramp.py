"""
https://leetcode.com/problems/maximum-width-ramp/description/?envType=daily-question&envId=2024-10-10
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.



Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.


Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104
"""

# Standard libraries
from typing import List


# Attempt 1
class Solution1:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_ = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i < j) and nums[i] <= nums[j]:
                    w = j - i
                    max_ = w if w > max_ else max_
        return max_


# Attempt 2
class Solution2:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_ = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i < j) and nums[i] <= nums[j]:
                    w = j - i
                    max_ = w if w > max_ else max_
        return max_
        # above work but indexing can be slow...
        # what about just the values and back out the index?


# Attempt 3
def get_diff(idx, val, space):
    candidates = [i + idx + 1 for i, x in enumerate(space) if x >= val]
    out = max(candidates) - idx if candidates else 0
    return out


class Solution3:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_ = 0
        for idx in range(len(nums)):
            val = nums[idx]
            space = nums[idx + 1 :]
            diff = get_diff(idx, val, space)
            max_ = diff if diff > max_ else max_
        return max_
        # print(val, space, diff)
        # print(val, space)


# print(get_diff(0, 6, [0, 8, 2, 1, 5]))
# # 6 [0, 8, 2, 1, 5]
# print(get_diff(1, 0, [8, 2, 1, 5]))
# # 0 [8, 2, 1, 5]
# print(get_diff(2, 8, [2, 1, 5]))
# # 8 [2, 1, 5]
# print(get_diff(3, 2, [1, 5]))
# # 2 [1, 5]
# print(get_diff(4, 1, [5]))
# # 1 [5]
# print(get_diff(5, 5, []))
# # 5 []


# Solution 1
class SolutionA:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        # Step 1: Build a decreasing stack of indices
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
                print(f'{stack=}')

        maxWidth = 0

        # Step 2: Traverse from the end and find maximum width ramp
        for j in range(n - 1, -1, -1):
            print(f'{j=}')
            while stack and nums[stack[-1]] <= nums[j]:
                maxWidth = max(maxWidth, j - stack.pop())
                print(f'{maxWidth=}')

        return maxWidth


# Standard libraries
# Solution 2
from itertools import accumulate
from operator import sub


class SolutionB:
    def maxWidthRamp(self, nums: List[int]) -> int:
        sorted_indices = [x[0] for x in sorted(enumerate(nums), key=lambda x: x[1])]
        min_sorted_indices = list(accumulate(sorted_indices, min))
        return max(map(sub, sorted_indices, min_sorted_indices))


# Third-party libraries
# Solution 3
import numpy as np


class SolutionC:
    def maxWidthRamp(self, nums: List[int]) -> int:
        sorted_indices = np.argsort(nums, kind='mergesort')
        cum_min_indices = np.minimum.accumulate(sorted_indices)
        return (sorted_indices - cum_min_indices).max()
