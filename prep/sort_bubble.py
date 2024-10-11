"""
Bubble Sort
-----------
Start at the beginning of the array and swap the first two elements if
the first is greater than the second. Then, go to the next pair, and so
on, continuously making sweeps of the array until it is sorted.
n doing so, the smaller times slowly "bubble" up to the beginning of the
list.

Runtime: O(n**2)
Memory: O(1)

Notes
-----
l1 = [5,4,3,2,1]

%timeit sort_bubble.bubble_sort_naive(l1)
3.01 µs ± 119 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit sort_bubble.bubble_sort(l1)
2.05 µs ± 9.07 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit sort_bubble.bubble_sort_early_stop(l1)
683 ns ± 23.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

l2 = [2,1,3,4,5]

%timeit sort_bubble.bubble_sort_naive(l2)
3 µs ± 189 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit sort_bubble.bubble_sort(l2)
2.08 µs ± 16.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit sort_bubble.bubble_sort_early_stop(l2)
668 ns ± 3.09 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

l3 = [1,2,3,4,5]

%timeit sort_bubble.bubble_sort_naive(l3)
2.96 µs ± 65.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit sort_bubble.bubble_sort(l3)
2.07 µs ± 27 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%timeit sort_bubble.bubble_sort_early_stop(l3)
687 ns ± 6.06 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
"""

# Standard libraries
from typing import List


def bubble_sort_naive(nums: List[int]) -> List[int]:
    for _ in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble_sort(nums: List[int]) -> List[int]:
    """More efficient and removes extra looping steps."""
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble_sort_early_stop(nums: List[int]) -> List[int]:
    """More efficient as only performs tasks when unsorted."""
    has_swapped = True
    n_iter = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(nums) - n_iter - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                has_swapped = True
        n_iter += 1

    return nums
