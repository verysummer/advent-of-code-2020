# -*- coding: utf-8 -*-

# AoC 2020 Day 3

import os
import numpy as np

os.chdir('C:/Users/Profil/Documents/adventofcode')

# open input
f = open('input3.txt','r')
f = f.readlines()

# make matrix (with numpy)
m = np.array(f)
print(m)

# tree counter
trees = 0

# start in first row first column
#r = 0
c = 0

for r in range(len(m[:])):
    position = m[r][c]
    print(position)
    
    if position == '#':
        print('encountered tree!')
        trees += 1
    
    # 3 right, 1 down
    c += 3
    #r += 1
    
    # if at the last element of the row or beyond
    if c >= len(m[0])-1:
        # go back to beginning
        c -= len(m[0])-1
    
print(trees)    
    
