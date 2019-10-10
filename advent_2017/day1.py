"""
Day 1:

Part 1:
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all
digits that match the next digit in the list. The list is circular, so the digit after the last
digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third
     digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.


Part 2:
Now, instead of considering the next digit, it wants you to consider the digit halfway around the
circular list. That is, if your list contains 10 items, only include a digit in your sum if the
digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.

Puzzle:
day1_puzzle.txt

Answers:
    Part 1: 1251
    Part 2: 1244
"""
from pathlib import Path


# No kwargs on purpose (for pytest)
def load_data():
    input_file_path = Path(__file__).parent.joinpath('data/day1_puzzle.txt')
    with open(input_file_path, 'r') as input_file:
        data = input_file.readline().strip()

    return data


# Part 1 Solution
def captcha1(data):
    """ Assumes data is a str """
    # Add first digit to end
    data = data + data[0]

    out = sum([int(a) for a,b in zip(data, data[1:]) if a == b])
    return out


# Part 2 Solution
def captcha2(data):
    """ Assumes data is a str """
    half_point = len(data) // 2
    first_half = data[:half_point]
    last_half  = data[half_point:]
    comp_data  = last_half + first_half

    out = sum([int(a) for a,b in zip(data, comp_data) if a == b])
    return out

