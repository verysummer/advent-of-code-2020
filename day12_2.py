# -*- coding: utf-8 -*-

# AoC 2020 Day 12

import os
import re

os.chdir('C:/Users/Profil/Documents/adventofcode')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input12.txt','r')
lines  = f.readlines()

data = []
for line in lines:
    if line[0] == 'L' or line[0] == 'R':
        line = line.replace('\n','')
        data.append(line) # don't split L and R
    else:
        data.append(re.split('(\d+)', line))
    
# test data 
#data = [['F', '10'], ['N', '3'], ['F', '7'], 'R90', ['F', '11']]
    
# start at position 0,0 and facing east
ship_pos = [0,0] # E,N --> relative to [0,0]
wp_pos = [10, 1] # E, N --> RELATIVE TO SHIP

for action in data:
    if action[0] == 'N':
        wp_pos[1] += int(action[1])
    elif action[0] == 'S':
        wp_pos[1] -= int(action[1])
    elif action[0] == 'E':
        wp_pos[0] += int(action[1])
    elif action[0] == 'W':
        wp_pos[0] -= int(action[1])
    elif action[0] == 'L' or action[0] == 'R':
        # current WP position:
        E = wp_pos[0]
        N = wp_pos[1]
        # rotate
        if action == 'R90' or action == 'L270':
            wp_pos = [N,-E]
        elif action == 'R180' or action == 'L180':
            wp_pos = [-E,-N]
        elif action == 'R270' or action == 'L90':
            wp_pos = [-N,E]
    elif action[0] == 'F':
        # new ship position: move in direction of WP
        E = ship_pos[0] + (wp_pos[0] * int(action[1]))
        N = ship_pos[1] + (wp_pos[1] * int(action[1]))
        ship_pos = [E,N]


# answer 2
manhatten = abs(ship_pos[0]) + abs(ship_pos[1])
print(manhatten)
