# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 22:14:46 2016

@author: thomlo02
"""

'''Create a program that asks the user to enter their name and age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
'''
from datetime import datetime

def when_100():
    name = input('Please enter your name: ' )
    age  = input('Please enter your age: ')
    try:
        diff = 100-int(age)
        curr_year = datetime.now().year
        print ('Hello {}! You will turn 100 in the year {}'.format(name, curr_year+diff))
    except:
        print ('Please enter an integer for your age')

if __name__ == '__main__':
    when_100()