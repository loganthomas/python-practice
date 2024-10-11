"""
Merge Sort
----------
Divide the array in half, sort each of those halves, and then merge them
back together. Each of those halves has the same sorting algorithm
applied to it. Eventually, you are merging just two single-element
arrays. It is the "merge" part that does the heavy lifting.

Runtime: O(n*log(n))
Memory: Depends
"""

from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) > 1:
        # Find midpoint of array
        mid = len(nums) // 2

        # Divide arrays into left and right sub-arrays
        L = nums[:mid]
        R = nums[mid:]

        # Recursive call to sort each half
        # Once sub-arrays are a single-element arrays, this call will
        # be skipped due to the len(nums) > 1 statement at start
        merge_sort(L)
        merge_sort(R)

        # Two iterators for traversing two halves (i and j)
        # One iterator for the main list (k)
        i = j = k = 0

        # This will put the smaller value at the start of the main array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        print(nums)

        # Check if any elements left over
        # This will fill in missing values to the main array that
        # weren't added above
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1

        print(nums)
    return nums
