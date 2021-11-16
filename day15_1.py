# -*- coding: utf-8 -*-

# AoC 2020 Day 14

import os
import numpy as np

os.chdir('C:/Users/Profil/Documents/adventofcode/2020/advent-of-code-2020/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
inpu = [18,11,9,0,5,1]
#inpu = [3,1,2] # test data
nums = np.array(inpu)

while len(nums) < 2020:
    if nums[-1] in nums[0:-1]:
        found = np.where(nums==nums[-1])
        last_i = found[0][-2] + 1 # find last occurence
        result = len(nums) - last_i
        nums = np.append(nums, result)
    else:
        nums = np.append(nums, 0)

print(nums[-1])