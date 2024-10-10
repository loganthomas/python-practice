"""
Two Sum Problem
---------------
See: https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than
O(n2) time complexity?
"""


class Solution:
    def brute_solution(self, nums, target):
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if (i != j) and (x + y == target):
                    return [i, j]

    def other_solution(self, nums, target):
        options = set(nums)
        for i, x in enumerate(nums):
            need = target - x
            if need in options:
                need_idx = nums.index(need)
                if i != need_idx:
                    return [i, need_idx]

    def twoSum(self, nums, target):
        idx_mapping = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in idx_mapping:
                return [idx_mapping[complement], i]
            idx_mapping[x] = i
