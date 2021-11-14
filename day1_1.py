# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# AoC 2020 Day 1

import os

os.chdir('C:/Users/Profil/Documents/adventofcode')

# open input
f = open('input1.txt','r')
f = f.readlines()
f = map(int,f)
f = list(f)
print(f)

# find two entries that sum up to 2020

for i in f:
    for j in f:
        if i + j == 2020:
            print(i)
            print(j)
            x = i * j

print(x)

