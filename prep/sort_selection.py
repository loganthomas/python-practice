"""
Selection Sort
--------------
Simple but inefficient.

Find the smallest element using a linear scan and move it to the front
(swapping it with the front element). Then, find the second smallest and
move it, again doing a linear scan. Continue doing this until all
elements are in place.

Runtime: O(n**2)
Memory: O(1)
"""

from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        min_index = i

        # Find min
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums
