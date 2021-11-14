# -*- coding: utf-8 -*-

# AoC 2020 Day 13

import os
import numpy as np

os.chdir('C:/Users/Profil/Documents/adventofcode')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input13.txt','r')
lines  = f.readlines()

depart = int(lines[0])

data = lines[1]
data = data.split(',')

busses = []
for bus in data:
    if bus.isdigit():
        busses.append(int(bus))
              
# test data
#depart = 939
#busses = [7, 13, 59, 31, 19]

# get waiting times
waiting_time = []

for bus in busses:
    wait = bus - (depart % bus)
    waiting_time.append(wait)
    
# get shortest waiting time and corresponding bus 
index_min = np.argmin(waiting_time)
my_bus = busses[index_min]
my_wait = waiting_time[index_min]

# answer 1
print(my_bus * my_wait)
    
    
    