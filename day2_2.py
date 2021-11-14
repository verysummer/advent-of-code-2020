# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# AoC 2020 Day 2

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
    number2 = int(numbers[1])
    # get letter:
    letter = split_line[1][0]
    print(letter)
    # get password:
    pw = split_line[2]
    print(pw[number1-1])
    print(pw[number2-1])
    
    # check if letter occurs in pw at 1 of specific positions
    if pw[number1-1] == letter:
        if pw[number2-1] == letter:
            curr_val = False
        else:
            curr_val = True
    else:
        if pw[number2-1] == letter:
            curr_val = True
        else:
            curr_val = False
        
    if curr_val:
        print('correct')
        valid += 1
    else:
        print('incorrect')
        invalid += 1
    
    del curr_val
    
print(valid)
    
    
    
