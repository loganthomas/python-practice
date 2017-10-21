"""
Practice Problem:
Given a list of length 1 or more of integers, return the difference
between the largest and smallest values in the list.
"""


def find_range(nums):
    """Find the range (highest value - lowest value) of a provided
    list of integers.

    Args:
        nums (list): List of integers.

    Returns:
        range (int): The highest value in the provided list minus
                     the lowest value in the provided list.
    """
    # Check that the list of integers has more than 1 value
    if len(nums) <= 1:
        raise ValueError('Enter a list of integers with more than one value')

    high = max(nums)

    low = min(nums)

    diff = high - low

    return diff


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    range_of_numbers = find_range(numbers)
    print('The range of {} is {}'.format(numbers, range_of_numbers))
