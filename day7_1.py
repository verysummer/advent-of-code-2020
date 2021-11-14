# -*- coding: utf-8 -*-

# AoC 2020 Day 4

import os
import re

os.chdir('C:/Users/Profil/Documents/adventofcode')

# function for finding a bag x in a list of bags and their contents,
# returning list of bags that contain x
def find_bag(bagx, list_of_bag_and_content):
    
    result_bags = []
    for content in list_of_bag_and_content:
        if bagx in content[1]:
            print(content[0])
            # bags of interest that contain bag x
            result_bags.append(content[0])
    
    return result_bags

# separate bag and content 
def read_data(path):
    f = open(path, 'r')
    bag_and_content = []
    for line in f.readlines():
        bag_and_content.append(line.split(' bags contain '))
    return bag_and_content



# use function to find all bags containing shiny gold, then   
# use function to find all bags containing bags found before and so on
bag_and_content = read_data('input7.txt')

# janni
outside_bags = set()
current_bags = {'shiny gold'}
seen_bags = set()

while len(current_bags) > 0:
    bag = current_bags.pop()
    if bag not in seen_bags:
        contained_in = find_bag(bag, bag_and_content)
        outside_bags.update(contained_in)
        current_bags.update(contained_in)
    seen_bags.add(bag)
    
number_of_bags = len(outside_bags)

def count_contained_bags(bag_and_content, current_bags, outside_bags):
    if not current_bags:
        return outside_bags
    bag = current_bags.pop()
    contained_in = find_bag(bag, bag_and_content)
    outside_bags.update(contained_in)
    current_bags.update(contained_in)
    return count_contained_bags(bag_and_content, current_bags, outside_bags)
    
        

# vreni
bags_oi = ['shiny gold']
all_result_bags = []
               
searching = True
while searching:
    new_bags_oi = []
    for bag_oi in bags_oi:
        result_bags = find_bag(bag_oi, bag_and_content)
        
        # add to bags of interest for next round
        new_bags_oi += result_bags
        # add to results
        all_result_bags += result_bags
        
    if not new_bags_oi: # empty
        searching = False
    else:
        bags_oi = new_bags_oi
        

print(len(set(all_result_bags)))











    