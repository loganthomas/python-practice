"""
Practice Problem:
Write a function that will return the number of even
numbers in a provided array.
"""


def count_evens(nums):
    """
    Count number of even numbers within a provided list or array.

    Args
        nums (list or array): Provided numbers to consider.

    Returns
        cnt (int): Number of evens in provided list/array of numbers.
    """
    cnt = sum([1 for num in nums if num % 2 == 0])
    return cnt


if __name__ == '__main__':
    import numpy as np

    x = [1, 2, 3]
    y = np.array([2, 4, 6])

    cnt_x = count_evens(x)
    cnt_y = count_evens(y)

    print('There are {} even numbers in {}'.format(cnt_x, x))
    print('There are {} even numbers in {}'.format(cnt_y, y))
