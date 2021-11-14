# -*- coding: utf-8 -*-

# AoC 2020 Day 8

import os

#os.chdir('C:/Users/Profil/Documents/adventofcode')
os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input8.txt','r')
lines  = f.readlines()

# seperate instruction in operation and argument 
instructions = []
for line in lines:
    instructions.append(line.split())

# start
accumulator = 0
beenthere = [] # save where I've been already
curr_instruction = 0 # start at 0

# go on until instruction was executed already
while curr_instruction not in beenthere:
    
    instruction = instructions[curr_instruction]
    
    if instruction[0] == 'acc':
        accumulator += int(instruction[1])
        beenthere.append(curr_instruction) # save where I've been
        curr_instruction += 1 # go one further        
    elif instruction[0] == 'jmp':
        beenthere.append(curr_instruction) # save where I've been
        curr_instruction += int(instruction[1]) # jump to specified instruction
    elif instruction[0] == 'nop':
        beenthere.append(curr_instruction) # save where I've been
        curr_instruction += 1 # go one further
        
# answer 1
print(accumulator)
