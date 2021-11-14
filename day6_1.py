# -*- coding: utf-8 -*-

# AoC 2020 Day 6

import os

os.chdir('C:/Users/Profil/Documents/adventofcode')

# open input
f = open('input6.txt','r')
lines = f.readlines()

## put each group in one line

groups = []
group = ''


for line in lines:
    if line != '\n':
        group += line
    else:
        group = group.replace('\n', ' ')
        groups.append(group)   
        group = ''
        
# add last group
group = group.replace('\n', ' ')
groups.append(group)
        

# find unique answers in each group

all_answers = []

for group in groups:
    group2 = group.replace(" ", "")
    answers = set(group2)
    all_answers.append(len(answers))

# answer part 1
print(sum(all_answers))
        


