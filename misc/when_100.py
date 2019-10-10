"""
Practice Problem:

Create a function that asks the user to enter their name and age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
"""

# Standard Libraries
from datetime import datetime


def when_100():
    """
    Ask a user for their name and age, then print a message to them
    specifying when they will turn 100.
    """

    # Ask user for their name
    name = input('Please enter your name: ')

    # Ask user for their age
    age = input('Please enter your age (rounding to nearest integer): ')

    # Error handling
    try:
        diff = 100 - int(age)
        curr_year = datetime.now().year
        hundo_year = curr_year + diff
        print('Hello {}! You will turn 100 in the year {}'.format(name, hundo_year))
    except ValueError as err:
        print('ValueError {}'.format(err))


if __name__ == '__main__':
    when_100()

