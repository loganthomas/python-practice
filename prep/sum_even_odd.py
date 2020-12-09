"""
Sum Even and Odd Without If Statement
-------------------------------------

Write a function that sums all the even numbers and odd numbers
separately in the range from 0 to n. You are only allowed to use
ONE for loop and no while or if conditions.



Notes
-----
"""
# Standard libraries
from typing import Tuple


def sum_even_odd_slicing(n: int) -> Tuple[int, int]:
    """ Assumes ordered range from 0 to n. """
    nums = [*range(n)]
    even_sum = sum(nums[::2])
    odd_sum = sum(nums[1::2])

    return even_sum, odd_sum


def sum_even_odd_mod(n: int) -> Tuple[int, int]:
    """ Handles case where a list of unordered numbers can be provided. """
    sum_even = 0
    sum_odd = 0

    for num in range(n):
        sum_even += num * (1 - num % 2)
        sum_odd += num * (num % 2)

    return sum_even, sum_odd
