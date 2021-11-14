# -*- coding: utf-8 -*-

# AoC 2020 Day 8

import os

#os.chdir('C:/Users/Profil/Documents/adventofcode')
os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input9.txt','r')
lines  = f.readlines()

data = []
for line in lines:
    data.append(int(line))
    
# test data
#data = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]


# start with preamble (0-25) 
preamble = 25

# from 25 to end of data
for my_number in range(preamble, len(data)):
    
    # previous 25 start and end
    start = my_number-preamble
    stop = my_number
    
    # find two numbers in previous 25 that add up to value in question
    for prev1 in range(start,stop):
        for prev2 in range(prev1+1,stop):
            if data[prev1] + data[prev2] == data[my_number]:
                print("found it: " + str(data[prev1]) + " + " + str(data[prev2]) + " = " + str(data[my_number]))
                break
        else:
            continue       
        break
    
    # if didn't break
    if prev1 == stop-1 and prev2 == stop-1:
        # answer 1
        print('not found! ' + str(data[my_number]))
        invalid_number = data[my_number]
        break
    




