"""
A new system policy has been put in place that requires all accounts to use a passphrase instead of
simply a password.
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Puzzle:
day_4_puzzle.txt

Answer:
    Part 1 = 383
    Part 2 =
"""

# Solution 1 Testing
with open('day4_puzzle.txt') as f:
    data = f.readlines()

data = [row.strip() for row in data]

cnt = 0
for i, row in enumerate(data):
    splits = row.split()
    if len(splits) == len(set(splits)):
        print('{} valid'.format(i))
        cnt += 1
    else:
        print(i)

### without explicit for loop
sum([1 for row in data if len(row.split()) == len(set(row.split()))])

