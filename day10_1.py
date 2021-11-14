# -*- coding: utf-8 -*-

# AoC 2020 Day 10

import os

#os.chdir('C:/Users/Profil/Documents/adventofcode')
os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input10.txt','r')
lines  = f.readlines()

data = []
for line in lines:
    data.append(int(line))
    
# test data
data = [16,10,15,5,1,11,7,19,6,12,4]
    
data.sort()    
  
outlet = [0]
builtin = [max(data)+3]

# put all together
adapters = outlet + data + builtin


# find differences and count
differences = []
ones = 0
threes = 0
for i in range(len(adapters)-1):
    diff = adapters[i+1] - adapters[i]
    differences.append(diff)
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1

# answer 1
print(ones*threes)


## part 2 

# save dispensable adapters
# dispensable = []
# for i in range(len(adapters)-2):
#     # if difference from i to i+2 is less than 4, i+1 can be left out
#     if adapters[i+2] - adapters[i] < 4:
#         dispensable.append(adapters[i+1])

# new

# function that proves whether adapter list is valid, i.e. no differences > 3
def is_valid(adapter_list):
    for i in range(len(adapter_list)-1):
        diff = adapter_list[i+1] - adapter_list[i]
        if diff <= 3:
            return True
        else:
            return False
               

is_valid(adapters)
            
            
# remove items and test whether still valid
for adapter in adapters[1:-1]: # don't remove first or last
    if is_valid(adapters.remove(adapter)):
        adapters.remove(adapter)
    








