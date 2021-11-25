# -*- coding: utf-8 -*-

# AoC 2020 Day 16

import os

os.chdir('C:/Users/Profil/Documents/adventofcode/2020/advent-of-code-2020/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')


# open input
f = open('input16.txt','r')
lines  = f.readlines()


rules = []
my_ticket = []
nearby_tickets = []

curr_data = 'rules';
for line in lines:
    if line == '\n':
        continue
    if 'your ticket' in line:
        curr_data = 'my_ticket'
        continue
    if 'nearby tickets' in line:
        curr_data = 'nearby_tickets'
        continue
        
    # split infos       
    if curr_data == 'rules':
        line = line.split(': ')
        line[1] = line[1].split(' or ')
        line[1][1] = line[1][1].replace('\n','')
        ranges = []
        for rangee in line[1]: 
            rangee = rangee.split('-')
            ranges.append(list(map(int, rangee)))
        line[1] = ranges
        rules.append(line)
    
    if curr_data == 'my_ticket':
        line = line.split(',')
        line = list(map(int, line))
        my_ticket.append(line)
    
    if curr_data == 'nearby_tickets':
        line = line.split(',')
        line = list(map(int, line))
        nearby_tickets.append(line)
        
        
# find invalid tickets
invalid_values = []
for ticket in nearby_tickets:
    ticket_valid = True 
    for value in ticket:
        # check rules
        for rule in rules: 
            curr_ranges = rule[1]
            # if a value in a ticket does not match any rules, the ticket is invalid
            if value < curr_ranges[0][0] or (value > curr_ranges[0][1] and value < curr_ranges[1][0]) or value > curr_ranges[1][1]:
                value_valid = False
            else:
                value_valid = True
                break
            
        if value_valid == False:
            invalid_values.append(value)
            ticket_valid = False
            break

print(sum(invalid_values))
     