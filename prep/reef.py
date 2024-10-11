"""
Stdin is a simple csv. Write a script that swaps the first column and
second column and prints output to stdout.

Given:
    1,2,3
    a,b,c

Output:
    2,1,3
    b,a,c

Given:
    1,"2,3",4

Output:
    "2,3",1,4
"""

import csv
import io
import sys


def swap_first_second_cols(row):
    # Handle double quotes parsing from csv
    if (row[1].startswith('"')) & (not row[1].endswith('"')):
        row[1] = ','.join([row[1], row[2]])
        row.pop(2)
    row[0], row[1] = row[1], row[0]
    return row


def main():
    data = sys.stdin.readlines()

    for row in csv.reader(data, quotechar="'"):
        swapped = swap_first_second_cols(row)
        print(','.join(swapped))


if __name__ == '__main__':
    # Setup problem 1
    sys.stdin = io.StringIO('1,2,3\na,b,c')
    print('Input:')
    for line in sys.stdin.readlines():
        print(line.strip())
    print('\nOutput:')
    sys.stdin = io.StringIO('1,2,3\na,b,c')
    main()
    print()

    # Setup problem 2
    sys.stdin = io.StringIO('1,"2,3",4')
    print('Input:')
    for line in sys.stdin.readlines():
        print(line.strip())
    print('\nOutput:')
    sys.stdin = io.StringIO('1,"2,3",4')
    main()
    print()

    # Unique Case...
    sys.stdin = io.StringIO('1,"2",3')
    print('Input:')
    for line in sys.stdin.readlines():
        print(line.strip())
    print('\nOutput:')
    sys.stdin = io.StringIO('1,"2",3')
    main()
    print()

    # Unique Case...
    sys.stdin = io.StringIO('1,"2",3\n4,"5,6","7",8,"9"')
    print('Input:')
    for line in sys.stdin.readlines():
        print(line.strip())
    print('\nOutput:')
    sys.stdin = io.StringIO('1,"2",3\n4,"5,6","7",8,"9"')
    main()
    print()
