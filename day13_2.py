# -*- coding: utf-8 -*-

# AoC 2020 Day 13

import os
import numpy as np

os.chdir('C:/Users/Profil/Documents/adventofcode')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input13.txt','r')
lines  = f.readlines()

#depart = int(lines[0])

data = lines[1]
data = data.split(',')

# test data
#data = ['67','7','x','59','61']

busses = []
for bus in data:
    if bus.isdigit():
        bus = int(bus)
        busses.append(bus)
              

# find least frequent bus and its offset (=index)
rare_bus = max(busses)
offset = data.index(str(rare_bus))

#my_time = 0 # start at minute 0
my_time = 99999999999563
running = True
while running:
    my_time += rare_bus
    timestamp = my_time - offset # departure times of least frequent bus minus its offset = timestamp (potential departure of first bus in list)
    # go through all busses and check if they arrive according to their offsets from timestamp, i.e. their index in the list       
    for b in range(len(data)): 
        if data[b].isdigit(): # is integer = is bus 
            if not((timestamp + b) % int(data[b]) == 0): # doesn't arrive at the right time
                break
    else: # if for loop completed normally, i.e. no break
        # found the right timestamp
        running = False
        
# answer 2
print(timestamp)
        








