"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/?envType=daily-question&envId=2024-10-13

632. Smallest Range Covering Elements from K Lists
Hard
Topics
Companies
You have k lists of sorted integers in non-decreasing order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d]
if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]


Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order
"""

# # Keep doing this until it reaches one of the lists' end (break)
import heapq
from collections import defaultdict

# import itertools

# First attempt failed below test:
# [[10, 10], [11, 11]]
# Need to handle empty potential range ends
# def smallest_range(nums):
#     maxes = [max(elements) for elements in nums]
#     min_maxes = min(maxes)
#     d_nums = dict(enumerate(nums))
#     d_nums = {k: [x for x in v if x > min_maxes] for k, v in d_nums.items()}

#     if all(x == [] for x in d_nums.values()):
#         return [nums[0][0], nums[0][0]]

#     candidates = sorted(itertools.chain.from_iterable(d_nums.values()))
#     potential_range_ends = []
#     for array_idx, candidates in d_nums.items():
#         others = [k for k in d_nums.keys() if k != array_idx and d_nums[k]]
#         print(others)
#         if candidates:
#             for candidate in candidates:
#                 for other in others:
#                     test_range = range(min_maxes, candidate)
#                     print(
#                         'this idx',
#                         array_idx,
#                         'this test range',
#                         test_range,
#                         'other',
#                         other,
#                     )
#                     bool_ = any(x in test_range for x in d_nums[other])
#                     print(bool_)
#                     if bool_:
#                         potential_range_ends.append(candidate)
#         return [min_maxes, min(potential_range_ends)]


# Second attempt failed below test:
# failed [[1],[2],[3],[4],[5],[6],[7]]
# Need collect all bools across others for eval not just single other
# def smallest_range(nums):
#     maxes = [max(elements) for elements in nums]
#     min_maxes = min(maxes)
#     d_nums = dict(enumerate(nums))
#     d_nums = {k: [x for x in v if x > min_maxes] for k, v in d_nums.items()}

#     if all(x == [] for x in d_nums.values()):
#         return [nums[0][0], nums[0][0]]

#     # candidates = sorted(itertools.chain.from_iterable(d_nums.values()))
#     potential_range_ends = []
#     for array_idx, candidates in d_nums.items():
#         others = [k for k in d_nums.keys() if k != array_idx and d_nums[k]]
#         print(others)
#         if candidates:
#             for candidate in set(candidates):
#                 for other in others:
#                     test_range = range(min_maxes, candidate)
#                     print(
#                         'this idx',
#                         array_idx,
#                         'this test range',
#                         test_range,
#                         'other',
#                         other,
#                     )
#                     bool_ = any(x in test_range for x in d_nums[other])
#                     print(bool_)
#                     if bool_:
#                         potential_range_ends.append(candidate)
#     end = min(potential_range_ends) if potential_range_ends else max(maxes)
#     return [min_maxes, end]


# Third attempt failed below test:
# [[-5, -4, -3, -2, -1, 1], [1, 2, 3, 4, 5]]
# Need to handle abs value
# Better: Use index and grab from list rather than value
# def smallest_range(nums):
#     maxes = [max(elements) for elements in nums]
#     min_maxes = min(maxes)
#     d_nums = dict(enumerate(nums))
#     d_nums = {k: [x for x in v if x > min_maxes] for k, v in d_nums.items()}

#     if all(x == [] for x in d_nums.values()):
#         return [nums[0][0], nums[0][0]]

#     # candidates = sorted(itertools.chain.from_iterable(d_nums.values()))
#     potential_range_ends = []
#     for array_idx, candidates in d_nums.items():
#         others = [k for k in d_nums.keys() if k != array_idx and d_nums[k]]
#         print(others)
#         if candidates:
#             for candidate in set(candidates):
#                 bools = []
#                 for other in others:
#                     test_range = range(min_maxes, candidate)
#                     print(
#                         'this idx',
#                         array_idx,
#                         'this test range',
#                         test_range,
#                         'other',
#                         other,
#                     )
#                     bool_ = any(x in test_range for x in d_nums[other])
#                     bools.append(bool_)
#                 print(bools)
#                 if all(bools):
#                     potential_range_ends.append(candidate)
#     end = min(potential_range_ends) if potential_range_ends else max(maxes)
#     return [min_maxes, end]


# Given solution 1
# Intuition
# The key takeaway is to utilize a min-heap to track the minimum
# element from each list and a sliding window to track the range of numbers.

# Approach
# Initialize a min-heap (smallest element from each list, list index,
# index of element within the list)
# Track current_max across all the k lists (for range)
# Iterate through the lists by always popping the minimum element
# from the heap (by heap's nature) and checking the range between
# the minimum and the current maximum.
# Update the smallest range whenever a smaller one is found.
# Push the next element from the same list (the list from which
# the popped element came) into the heap. Update the current maximum as necessary.
# Stop the iteration once any list runs out of elements.
# Example
# nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# # Heap initialization (element, list_idx, idx)
# Heap: [(0, 1, 0), (4, 0, 0), (5, 2, 0)]

# # Popping from this heap will result in returning (0, 1, 0)
# Heap: [(4, 0, 0), (5, 2, 0)]

# # After range updates, push the next element in 1st list to heap
# Heap:  [(4, 0, 0), (5, 2, 0), (9, 1, 1)]
# # since it was 9 (bigger than 4 & 5), it goes to the end


def smallest_range(nums):
    heap = []
    cur_max = float('-inf')

    # find min of all elements of nums
    # store as (element, nums idx, element idx)
    for nums_idx, elements in enumerate(nums):
        # since nums have sorted elements, know min is at idx 0
        min_idx = 0
        heapq.heappush(heap, (elements[min_idx], nums_idx, min_idx))
        cur_max = max(cur_max, elements[min_idx])
        print(f'{cur_max=}')
        # example 1
        # heap = [(0,1,0), (4,0,0), (5,2,0)]
        # curr_max = 5

    range_ = [float('-inf'), float('inf')]
    while heap:
        print(f'{range_=}')
        print(f'{heap=}')
        print(f'{cur_max=}')

        cur_min, nums_idx, min_idx = heapq.heappop(heap)
        print(f'{cur_min=} {nums_idx=} {min_idx=}')

        # update range_ if a smaller one is found
        if cur_max - cur_min < range_[1] - range_[0]:
            print(f'Updating range_ from {range_=}...')
            range_ = [cur_min, cur_max]
            print(f'to {range_=}...')

        # check if next min_idx is valid in range of nums element
        # (i.e. think of nums[nums_idx] is an element of nums)
        if min_idx + 1 < len(nums[nums_idx]):
            next_ = nums[nums_idx][min_idx + 1]
            print(f'Moving to {next_=}')
            heapq.heappush(heap, (next_, nums_idx, min_idx + 1))
            print(f'{heap=}')
            print(f'Updating curr_max from {cur_max=}...')
            cur_max = max(cur_max, next_)
            print(f'tp {cur_max=}...')
        # Hit an end point of an element so stop
        else:
            break
    return range_


# Solution 2
# Keeping track of the locations, ensuring all 3 are there
# Finding smallest range once all three are accounted for


def smallest_range2(nums):
    # List to store all numbers with their list index
    # Populate the ordered list with all numbers and their corresponding list index
    # Sort the ordered list based on the numbers
    ordered = sorted([(n, nums_idx) for nums_idx, elements in enumerate(nums) for n in elements])
    # print(f'{ordered=}')

    # i: start of current range, k: count of unique lists covered
    range_start, n_elements_covered = 0, 0
    # print(f'{range_start=}')
    # print(f'{n_elements_covered=}')

    # List to store the final answer (smallest range)
    ans = []
    # Dictionary to keep track of number of elements from each list that have been touched
    count = defaultdict(int)
    # print(f'{ans=}')
    # print(f'{count=}')

    # Iterate through the sorted ordered list
    for value, nums_idx in ordered:
        # print(f'{value=} {nums_idx=}')

        # If this is a new list or increment the count for this list
        if count[nums_idx] == 0:
            n_elements_covered += 1
        count[nums_idx] += 1
        # print(f'{count=}')
        # print(f'{n_elements_covered=}')

        # If we have covered all lists
        if n_elements_covered == len(nums):
            # Shrink the range from the start while maintaining coverage of all lists
            # get all covered lists down to touching one element
            while count[ordered[range_start][1]] > 1:
                # print('updating...')
                # print(f'{range_start=}')
                # print(f'{ordered[range_start]=}')
                # print(f'{count[ordered[range_start][1]]=}')
                count[ordered[range_start][1]] -= 1
                range_start += 1
                # print(f'updated {count=}')
                # print(f'updated {range_start=}')

            # Update the answer if this is the first valid range or if it's smaller than the previous range
            if not ans or ans[1] - ans[0] > value - ordered[range_start][0]:
                ans = [ordered[range_start][0], value]
            # print(f'{ans=}')
    return ans  # Return the smallest range that includes at least one number from each list
