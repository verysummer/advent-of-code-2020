# -*- coding: utf-8 -*-

# AoC 2020 Day 6

import os

#os.chdir('C:/Users/Profil/Documents/adventofcode')
os.chdir('C:/Users/vrsom/Seafile/adventofcode')

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
        

## separet people within groups and find common answers
all_answers = []

for group in groups:
    split_group = group.split()
    
    # finds intersection in all lists
    answers = set(split_group[0]).intersection(*split_group[1:])
   
    all_answers.append(len(answers))
    

# answer part 2
print(sum(all_answers))
        


