# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:23:30 2016

@author: thomlo02
"""
import pandas as pd


def fizzbuzz(list):
    output = []
    for x in list:
        if x % 15 == 0:
            output.append('Fizzbuzz')
        elif x % 3 == 0:
            output.append('Fizz')
        elif x % 5 == 0:
            output.append('Buzz')
        else:
            output.append(x)
    return output


func_output = fizzbuzz(range(1, 101))


# Validation df
df = pd.DataFrame([x for x in range(1, 101)])
df['mod3'] = df[0] % 3
df['mod5'] = df[0] % 5
df['mod15'] = df[0] % 15

# Output column to validate
df['output'] = func_output

# Checks
df[(df['mod3'] == 0) & (df['mod5'] != 0) & (df['mod15'] != 0)]  # Fizz
df[(df['mod3'] != 0) & (df['mod5'] == 0) & (df['mod15'] != 0)]  # Buzz
df[df['mod15'] == 0]  # Fizzbuzz
