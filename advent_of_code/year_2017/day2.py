"""
Day 2:

Part 1:
The spreadsheet consists of rows of apparently-random numbers.
To make sure the recovery process is on the right track, they need you to calculate the
spreadsheet's checksum. For each row, determine the difference between the largest value and the
smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?


Part 2:
"Based on what we're seeing, it looks like all the User wanted is some information about the evenly
divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of
calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the
other - that is, where the result of the division operation is a whole number. They would like you
to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2;
   the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.


Puzzle:
day2_puzzle.txt

Answer:
    Part 1: 41887
    Part 2: 226
"""
import numpy as np
from pathlib import Path


# No kwargs on purpose (for pytest)
def load_data():
    input_file_path = Path(__file__).parent.joinpath('data/day2_puzzle.txt')
    data = np.loadtxt(input_file_path)
    return data


# Part 1 Solution
def captcha1(data):
    """ Assumes data is np.array """
    # Max of each row
    maxes = data.max(axis=1)

    # Mins of each row
    mins = data.min(axis=1)

    checksum = sum(maxes - mins)
    return checksum


# Part 2 Solution
def captcha2(data):
    """ Assumes data is np.array """
    out = []
    for row in data:
        sort = sorted(row, reverse=True)

        for n in sort:
            idx = sort.index(n)
            comps = sort[idx + 1:]

            for c in comps:
                if n % c == 0:
                    out.append(n / c)

    return sum(out)

