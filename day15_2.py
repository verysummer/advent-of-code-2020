# -*- coding: utf-8 -*-

# AoC 2020 Day 15

import os
import numpy as np

os.chdir('C:/Users/Profil/Documents/adventofcode/2020/advent-of-code-2020/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
inpu = [18,11,9,0,5,1]
#inpu = [3,1,2] # test data
inpu = np.array(inpu)

# make dictionary with numbers pointing to their index in the list
nums = {}
for num in inpu[0:-1]: # except last number
    nums[num] = np.where(inpu==num)[0][0] + 1

cnt = len(inpu)
curr_num = inpu[-1] # start with last number 

while cnt < 30000000:
    if curr_num in nums: # is key?
        # get last occurence (index)
        last_i = nums[curr_num]   
        # current number points to current index (counter)
        nums[curr_num] = cnt
        # next number is difference of indices
        curr_num = cnt - last_i
        
    else:
        # current number points to current index (counter)
        nums[curr_num] = cnt
        # next number is 0
        curr_num = 0
    
    cnt += 1


print(curr_num)
