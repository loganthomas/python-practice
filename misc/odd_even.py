"""
Practice Problem:

Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user.
"""


def odd_even():
    """
    Ask the user for a number and print whether
    the number is odd or even.

    Returns
        print statement whether provided number is odd or even.
    """
    # Ask user for number
    number = input('Please enter a number: ')

    # Error handling
    try:
        num = int(number)

        # Determine odd or even
        if int(num) % 2 == 0:
            print('{} is even'.format(number))
        else:
            print('{} is odd'.format(number))

    except ValueError as err:
        print('Value Error: {}'.format(err))


if __name__ == '__main__':
    odd_even()

