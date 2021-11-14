# -*- coding: utf-8 -*-

# AoC 2020 Day 12

import os
import re

#os.chdir('C:/Users/Profil/Documents/adventofcode')
os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input12.txt','r')
lines  = f.readlines()

data = []
for line in lines:
    data.append(re.split('(\d+)', line))
    
# test data 
#data = [['F', '10'], ['N', '3'], ['F', '7'], ['R', '90'], ['F', '11']]
    
# start at position 0,0 and facing east
curr_pos = [0,0] # E,N
face = 90 # 0 = north, 90 = east, 180 = south, 270 = west, 360 = 0 = north

for action in data:
    action[1] = int(action[1])
    if action[0] == 'N':
        curr_pos[1] += action[1]
    elif action[0] == 'S':
        curr_pos[1] -= action[1]
    elif action[0] == 'E':
        curr_pos[0] += action[1]
    elif action[0] == 'W':
        curr_pos[0] -= action[1]
    elif action[0] == 'L':
        face -= action[1]
    elif action[0] == 'R':
        face += action[1]
    elif action[0] == 'F':
        if face == 0: # north
            curr_pos[1] += action[1]
        elif face == 180: # south
            curr_pos[1] -= action[1]
        elif face == 90: # east
            curr_pos[0] += action[1]
        elif face == 270: # west
            curr_pos[0] -= action[1]
    
    if face >= 360:
        face -= 360
    elif face < 0:
        face += 360

# answer 1
manhatten = abs(curr_pos[0]) + abs(curr_pos[1])
print(manhatten)
