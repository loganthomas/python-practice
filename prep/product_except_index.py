"""
Product of Integers Except at Index
-----------------------------------

You have an array of integers, and for each index you want to find the
product of every integer except the integer at that index.

For example, given:

[1, 7, 3, 4]

Your method would return:

[84, 12, 28, 21]

by calculating:

[7*3*4, 1*3*4, 1*7*4, 1*7*3]

Notes
-----
"""
# Standard libraries
from typing import List


def find_products_with_division(nums: List[int]) -> List[int]:
    # numerator = functools.reduce(lambda x,y: x*y, nums)
    numerator = 1
    for x in nums:
        numerator *= x

    out = []
    for x in nums:
        try:
            prod = int(numerator / x)
        except ZeroDivisionError:
            prod = 0
        out.append(prod)

    return out


# Now you are not allowed to use division
def find_products_without_division(nums: List[int]) -> List[int]:
    out = []

    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                prod *= nums[j]
        out.append(prod)

    return out


# The above solution works, but it is O(n**2).
# Can you write a O(n) solution?
def find_products_optimized(nums: List[int]) -> List[int]:
    out = [None] * len(nums)

    # Before index products
    prod = 1
    for i in range(len(nums)):
        out[i] = prod
        prod *= nums[i]

    # After index products
    prod = 1
    for i in reversed(range(len(nums))):
        out[i] *= prod
        prod *= nums[i]

    return out
