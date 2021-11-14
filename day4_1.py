# -*- coding: utf-8 -*-

# AoC 2020 Day 4

import os

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

    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID) 
    # cid (Country ID) --> optional 

valid = 0
for curr_passport in passport_dicts:
    if 'byr' in curr_passport and 'iyr' in curr_passport and 'eyr' in curr_passport and 'hgt' in curr_passport and 'hcl' in curr_passport and 'ecl' in curr_passport and 'pid' in curr_passport:
        valid += 1
        print('valid')
    else:
        print('invalid')
   
print(valid)
        
        










