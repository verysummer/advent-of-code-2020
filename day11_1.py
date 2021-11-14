# -*- coding: utf-8 -*-

# AoC 2020 Day 11

import os

#os.chdir('C:/Users/Profil/Documents/adventofcode')
os.chdir('C:/Users/vrsom/Seafile/adventofcode')

# open input
f = open('input11.txt','r')
lines  = f.readlines()

test = []
for line in lines:
    test.append(line.replace('\n',''))

# test data
test = [ \
'L.LL.LL.LL', \
'LLLLLLL.LL', \
'L.L.L..L..', \
'LLLL.LL.LL', \
'L.LL.LL.LL', \
'L.LLLLL.LL', \
'..L.L.....', \
'LLLLLLLLLL', \
'L.LLLLLL.L', \
'L.LLLLL.LL']
    
# separate every character
data = []
for t in test:
    data.append(list(t))


# function to find adjacent seats, given data 
# and row and coloumn of seat in question (int)
def find_adjacent(data, row, col):
    adj_row = [row]
    adj_col = [col]
    if row > 0:
        adj_row.append(row-1)
    if row < len(data)-1:
        adj_row.append(row+1)
    if col > 0:
        adj_col.append(col-1)
    if col < len(data[0])-1:
        adj_col.append(col+1)
    
    # get all adjacent seats
    adj_seats = []
    for r in adj_row:
        for c in adj_col:
            # not the input seat and not floor (.)
            if not(r == row and c == col) and not(data[r][c] == '.'):
                adj_seats.append([r,c])
                
    return adj_seats


# apply rules until nothing changes anymore
something_changed = True
cnt = 0
while something_changed:

    # new data without any seats
    new_data = [['.'] * len(data[0]) for i in range(len(data))]
    
    # round of rules
    for row in range(len(data)):
        for seat in range(len(data[row])):
            # current seat and its adjacents
            my_seat = data[row][seat]
            adj_seats = find_adjacent(data,row,seat)
            # if it's empty
            if my_seat == 'L': 
                # check whether all adjacents are empty
                all_empty = True
                for adj_seat in adj_seats:
                    if data[adj_seat[0]][adj_seat[1]] == '#': # occupied
                        all_empty = False
                # if all adjacents are empty, current seat will become occupied (in new_data)
                if all_empty:
                    new_data[row][seat] = '#'
                else:
                    new_data[row][seat] = 'L'
            # if it's occupied
            if my_seat == '#':
                # check whether 4 or more adjacents are occupied
                occupied = 0 # counter
                for adj_seat in adj_seats:
                    if data[adj_seat[0]][adj_seat[1]] == '#': # occupied
                        occupied += 1
                # if 4 or more occupied, current seat will become empty 
                if occupied >= 4:
                    new_data[row][seat] = 'L'
                else:
                    new_data[row][seat] = '#'
    
    # check whether anything chnaged
    if data == new_data:
        something_changed = False
        
    data = new_data
    cnt += 1

# --> people stopped moving around

# count number of occupied seats
occupied = 0
for row in data:
    occupied += row.count('#')

# answer 1
print(occupied)

