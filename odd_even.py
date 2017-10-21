# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 22:27:57 2016

@author: thomlo02
"""

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

number = input ('Please enter a number: ')
try:
    num = int(number)
    if num%2==0:
        print(num, 'is an even number')
    else:
        print(num, 'is an odd number')
except:
    print('Please enter an integer value')