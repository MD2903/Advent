#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:35:28 2020

@author: martijn
"""

import numpy as np
import re
from timeit import default_timer as timer

file = open("/Users/martijn/Documents/Universiteit/Programmeren/advent/dag_4.txt").read()

start = timer()

def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

data = split_on_empty_lines(file)

#%%

def criterion(string):
    if 'byr' not in string:
        return False
    if 'iyr' not in string:
        return False
    if 'eyr' not in string:
        return False
    if 'hgt' not in string:
        return False
    if 'hcl' not in string:
        return False
    if 'ecl' not in string:
        return False
    if 'pid' not in string:
        return False
    else:
        return True

counter = 0
for ii in range(len(data)):
    if criterion(data[ii]) == True:
        counter += 1
        
#%%

def in_set(string):
    charRe = re.compile(r'[^a-f0-9.]')
    string = charRe.search(string)
    return not bool(string)

def criterion(string):
    passport = string.split()
    valid = 0
    for ii in range(len(passport)):
        statement = passport[ii].split(':')
        if statement[0] == 'byr' and 1920 <= int(statement[1]) <= 2002:
            valid += 1
        if statement[0] == 'iyr' and 2010 <= int(statement[1]) <= 2020:
            valid += 1
        if statement[0] == 'eyr' and 2020 <= int(statement[1]) <= 2030:
            valid += 1
        if statement[0] == 'hgt':
            if statement[1][-2:] == 'in' and 59 <= int(statement[1][:-2]) <= 76:
                valid += 1
            if statement[1][-2:] == 'cm' and 150 <= int(statement[1][:-2]) <= 193:
                valid += 1
        if statement[0] == 'hcl' and statement[1][0] == '#' and len(statement[1][1:]) == 6 and in_set(statement[1][1:]) == True:
            valid += 1
        if statement[0] == 'ecl' and statement[1] in ['amb','blu','brn','gry','grn','hzl','oth']:
            valid += 1
        if statement[0] == 'pid' and len(statement[1]) == 9:
            valid += 1
    if valid == 7:
        return True
    else:
        return False

counter = 0
for ii in range(len(data)):
    # print(criterion(data[ii]))
    if criterion(data[ii]) == True:
        counter += 1

end = timer()

print(end-start)
    
        
        
        
        
        
        
        
    

