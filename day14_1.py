# -*- coding: utf-8 -*-

# AoC 2020 Day 14

import os
import numpy as np

os.chdir('C:/Users/Profil/Documents/adventofcode')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input14.txt','r')
lines  = f.readlines()


# test data
#lines = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n', 'mem[8] = 11\n', 'mem[7] = 101\n', 'mem[8] = 0\n']

# array of zeros
all_results = {}

for line in lines:
    # get mask / values
    if 'mask = ' in line:
        line = line.split('= ')       
        mask = line[1]
        mask = mask.replace('\n','')
    elif 'mem' in line:
        line = line.split('= ')
        
        # extract memory address
        mem = line[0].replace('mem[','')
        mem = mem.replace(']','')
        mem = mem.strip()
        
        # extract binary and add zeros   
        value = bin(int(line[1]))
        value = value.split('b')[1]
        missing_zeros = len(mask) - len(value)
        value = '0' * missing_zeros + value
        
        # apply mask to value
        result = ''
        for i in reversed(range(len(mask))): # from last to first index
            if mask[i] == 'X':
                # does not change value
                result = value[i] + result # append to left of string
            else:
                # change value to mask
                result = mask[i] + result # append to left of string
                
        # convert to decimal and sacve to specific memory address
        all_results[mem] = int(result,2) 
        
# sum up 
print(sum(all_results.values()))



