# -*- coding: utf-8 -*-

# AoC 2020 Day 8

import os

#os.chdir('C:/Users/Profil/Documents/adventofcode')
os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input8.txt','r')
lines  = f.readlines()

# seperate instruction in operation and argument 
#orig_instructions = []
#for line in lines:
#    orig_instructions.append(line.split())
    
    
# change all jmp and nop instructions one by one
for i in range(len(lines)-1):    
    #print(i)
    
    # start (again) with original
    # seperate instruction in operation and argument 
    instructions = []
    for line in lines:
        instructions.append(line.split())
    
    # makes changes in new_instructions! 
    instruction = instructions[i]
    if instruction[0] == 'jmp':
        instruction[0] = 'nop'
        print('change jmp to nop')
    elif instruction[0] == 'nop':
        instruction[0] = 'jmp'
        print('change nop to jmp')
    else:
        continue
    

    # start from beginnning
    accumulator = 0
    beenthere = [] # save where I've been already
    curr_instruction = 0 # start at 0
    
    # go on until instruction was executed already (loop) or terminates 
    no_loop = True
    not_terminated = True
    while no_loop and not_terminated:
        
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
            
        # check whether terminates normally
        if curr_instruction >= len(instructions):
            print('terminated normally')
            not_terminated = False
        # or because of loop
        elif curr_instruction in beenthere:
            print('stuck in loop')
            no_loop = False
               
    # answer 2
    print(accumulator)
    
    # found solution such that it terminates
    if not_terminated == False:
        break





