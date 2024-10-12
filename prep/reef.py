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

###############################
# Original Interview Solution #
###############################
# def swap_first_second_cols(row):
#     # Handle double quotes parsing from csv
#     if (row[1].startswith('"')) & (not row[1].endswith('"')):
#         row[1] = ','.join([row[1], row[2]])
#         row.pop(2)
#     row[0], row[1] = row[1], row[0]
#     return row


# def main():
#     data = sys.stdin.readlines()

#     for row in csv.reader(data, quotechar="'"):
#         swapped = swap_first_second_cols(row)
#         print(','.join(swapped))
###############################


def swap_cols():
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)

    for row in reader:
        row[0], row[1] = row[1], row[0]
        writer.writerow(row)


if __name__ == '__main__':
    print('Problem 1')
    given = '1,2,3\na,b,c'
    print('Given:')
    print(given)
    print('Output:')
    sys.stdin = io.StringIO(given)
    swap_cols()
    print()
    print('Problem 2')
    given = '1,"2,3",4'
    print('Given:')
    print(given)
    print('Output:')
    sys.stdin = io.StringIO(given)
    swap_cols()
