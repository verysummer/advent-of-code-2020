# -*- coding: utf-8 -*-

# AoC 2020 Day 4

import os
import re

os.chdir('C:/Users/Profil/Documents/adventofcode')

# open input
f = open('input4.txt','r')
lines = f.readlines()

## make dictionary with passport data

passports = []
passport = ''

for line in lines:
    if line != '\n':
        passport += line
    else:
        passport = passport.replace('\n', ' ')
        passports.append(passport)   
        passport = ''
        
# add last passport
passports.append(passport)
        
# save in dict        
passport_dicts = []

for p in passports:
    # split entries at space
    split_passport = p.split()
    
    passport_dict = {}
    for entry in split_passport:
        split_entry = entry.split(':')
        key = split_entry[0]
        value = split_entry[1]
        passport_dict[key] = value
        
    passport_dicts.append(passport_dict)
        
    
## prove passport validity

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # (cid (Country ID) - ignored, missing or not.)


valid = 0
for curr_passport in passport_dicts:
    
    # check whether all keys exist
    if 'byr' in curr_passport and 'iyr' in curr_passport and 'eyr' in curr_passport and 'hgt' in curr_passport and 'hcl' in curr_passport and 'ecl' in curr_passport and 'pid' in curr_passport:
        
        # for checking hight
        hight = re.split('(\d+)', curr_passport['hgt'])
        for val in hight:
            if val.isdigit():
                hgt_val = int(val) 
            elif val == 'cm':
                hgt_unit = 'cm'
            elif val == 'in':
                hgt_unit = 'in'
                
        # for checking hair color
        hair = False
        if curr_passport['hcl'][0] == '#' and len(curr_passport['hcl']) == 7:
            for sign in curr_passport['hcl'][1:7]:
                if sign.isdigit() or sign in ['a','b','c','d','e','f']:
                    hair = True              
    
        # check all:
        if curr_passport['byr'].isdigit() and int(curr_passport['byr']) >= 1920 and int(curr_passport['byr']) <= 2020 \
            and curr_passport['iyr'].isdigit() and int(curr_passport['iyr']) >= 2010 and int(curr_passport['iyr']) <= 2020 \
            and curr_passport['eyr'].isdigit() and int(curr_passport['eyr']) >= 2020 and int(curr_passport['eyr']) <= 2030 \
            and ((hgt_unit == 'cm' and hgt_val >= 150 and hgt_val <= 193) or (hgt_unit == 'in' and hgt_val >= 59 and hgt_val <= 76)) \
            and hair \
            and curr_passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] \
            and curr_passport['pid'].isdigit() and len(curr_passport['pid']) == 9:
                
            valid += 1
            print('valid')
        else:
            print('invalid')
            
    else:
        print('invalid')
   
print(valid)
        
        


