# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# AoC 2020 Day 1

import os

os.chdir('C:/Users/Profil/Documents/adventofcode')

# open input
f = open('input2.txt','r')
f = f.readlines()

valid = 0
invalid = 0

# check every line
for lines in f:
    split_line = lines.split() # splits line at spaces
    print(split_line)
    numbers = split_line[0].split('-') # splits first list item at "-" 
    # get both numbers:
    number1 = int(numbers[0])
    print(number1)
    number2 = int(numbers[1])
    print(number2)
    # get letter:
    letter = split_line[1][0]
    print(letter)
    # get password:
    pw = split_line[2]
    # find letter in pw
    result = pw.count(letter)
    print(result)
    # check if occurs for right number
    if result >= number1 and result <= number2:
        print('correct')
        valid += 1
    else:
        print('incorrect')
        invalid += 1
    
print(valid)
    
    
    
