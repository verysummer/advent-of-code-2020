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

# start in first row first column
#r = 0
c = 0

# first 4 slopesd (with 1 down)
rights = [1,3,5,7]
all_trees = []

for right in rights:
    print("NEXT SLOPE")
    # tree counter
    trees = 0
        
    # for all rows
    for r in range(len(m[:])):
        
        position = m[r][c]
        print(position)

        if position == '#':
            print('encountered tree!')
            trees += 1
        
        # 3 right, 1 down
        c += right
        #r += 1
        
        # if at the last element of the row or beyond
        if c >= len(m[0])-1:
            # go back to beginning
            c -= len(m[0])-1

    print(trees)    
    
    all_trees.append(trees)    
    


# last slope (1 right 2 down)

# start in first row first column
r = 0
c = 0
trees = 0

# for all rows
for i in range(len(m[:])):
    
    position = m[r][c]
    print(position)

    if position == '#':
        print('encountered tree!')
        trees += 1
    
    # 3 right, 1 down
    c += right
    #r += 1
    
    # if at the last element of the row or beyond
    if c >= len(m[0])-1:
        # go back to beginning
        c -= len(m[0])-1

print(trees)    

all_trees.append(trees)    


result = all_trees[0] * all_trees[1] * all_trees[2] * all_trees[3] * all_trees[4] 
print(result)
