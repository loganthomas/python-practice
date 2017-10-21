# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:47:26 2016

@author: thomlo02
"""

'''Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''


def compare_lists():
    list1 = input('Please enter numbers in list1 seperated by a comma: ')
    list2 = input('Please enter numbers in list2 seperated by a comma: ')

    list1 = [int(x) for x in list1.split(',')]
    list2 = [int(x) for x in list2.split(',')]
    print(sorted(list(set(list1).intersection(list2))))


if __name__ == '__main__':
    compare_lists()
