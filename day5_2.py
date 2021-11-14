# -*- coding: utf-8 -*-

# AoC 2020 Day 5

import os
import math
import matplotlib.pyplot as plt


os.chdir('C:/Users/Profil/Documents/adventofcode')

# open input
f = open('input5.txt','r')
lines = f.readlines()

seats = []

for line in lines:
    row_min = 0
    row_max = 127
    row_diff = row_max - row_min
    col_min = 0
    col_max = 7
    col_diff  = col_max - col_min
    
    for letter in line:
        if letter == 'F':
            row_max = row_min + math.floor(row_diff/2)
            row_diff = row_max - row_min
        elif letter == 'B':
            row_min = row_min + math.ceil(row_diff/2)    
            row_diff = row_max - row_min
        elif letter == 'L':
            col_max = col_min + math.floor(col_diff/2)
            col_diff  = col_max - col_min
        elif letter == 'R':
            col_min = col_min + math.ceil(col_diff/2)
            col_diff  = col_max - col_min
            
    seats.append(row_min * 8 + col_min)
        
# answer part 1
print(max(seats))
    
seats.sort()

plt.style.use('seaborn-white')
x = list(range(len(seats)))
plt.plot(x, seats)
plt.show

for seat in range(min(seats),max(seats)):
    if seat not in seats:
        # answer part 2
        print(seat)

