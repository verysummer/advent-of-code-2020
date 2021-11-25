# -*- coding: utf-8 -*-

# AoC 2020 Day 18

import os

os.chdir('C:/Users/Profil/Documents/adventofcode/2020/advent-of-code-2020/')
#os.chdir('C:/Users/vrsom/Seafile/adventofcode')


# open input
f = open('input18.txt','r')
lines  = f.readlines()


# takes input of list of 3 items (number, operator, number) and returns the result
def compute(list3): 
    # joins list strings into one string and evaluates the calculation 
    result = eval(' '.join(list3))
    return str(result)


# takes input of equation without brackets (string) and solves equation
# from left to right (without operator precedence), returns result
def solve_equation(equation):
    equation = equation.split()
    done = False
    while not(done):
        list3 = equation[0:3] # first 3 items
        result = compute(list3) # evaluate
        list_rest = equation[3:len(equation)+1] # rest of list 
        if list_rest == []:
            grand_result = result
            done = True
        else:
            # update equation
            equation = [result] + list_rest
            
    return grand_result

# try
x = solve_equation('1 + 2 * 3 + 4 * 5 + 6')


# test
equation = '1 + (2 * 3) + (4 * (5 + 6))'

result_found = False
while not(result_found):
    # solve equations in brackets until there are no brackets anymore
    if '(' in equation:
        # separate equation in first innermost brackets 
        temp_equation = equation
        innermost = False
        while not(innermost):
            if '(' in temp_equation: 
                # find first opening brackets
                open_br = temp_equation.find('(')
                # find first closing brackets
                close_br = temp_equation.find(')')
                # use subset as new equation and
                # check whether other brackets in-between
                temp_equation = temp_equation[open_br+1:close_br]
                
            else: # found innermost
                innermost = True
        
        # solve equation in innermost brackets and replace with result
        inner_result = solve_equation(temp_equation)
        temp_equation = '(' + temp_equation + ')' # add brackets around
        equation = equation.replace(temp_equation, inner_result)
    
    else: # no brackets anymore
        result_found = True

