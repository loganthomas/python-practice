"""
Practice Problem:
Write a function that will take two numbers and return the sum.
"""


def add_two(a, b):
    """
    Add two numbers together.

    Args:
       a (int or float): First number.
       b (int or float): Second number.

    Returns:
        added (int or float): Sum of a and b.
    """
    # Check both input values are either an float or integer
    if type(a) not in (float, int):
        raise TypeError('Enter a valid integer or float for first variable')
    if type(b) not in (float, int):
        raise TypeError('Enter a valid float or integer for second variable')

    # Add two given values together
    added = a + b

    return added


if __name__ == '__main__':
    val1 = float(input('Enter value 1: '))
    val2 = float(input('Enter value 2: '))
    added = add_two(val1, val2)
    print('{} plus {} is {}'.format(val1, val2, added))
