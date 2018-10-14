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
    # Add numbers together if possible
    try:
        float_a = float(a)
        float_b = float(b)
        return float_a + float_b

    # Catch error if not able to add
    except Exception as e:
        print(e)


if __name__ == '__main__':
    val1 = input('Enter value 1: ')
    val2 = input('Enter value 2: ')
    added = add_two(val1, val2)
    if added:
        print('{} plus {} is {}'.format(val1, val2, added))

