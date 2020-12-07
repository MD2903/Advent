#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:50:47 2020

@author: martijn
"""

import numpy as np
import re

file = open("/Users/martijn/Documents/Universiteit/Programmeren/advent/dag_6.txt").read()

def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

data = split_on_empty_lines(file)

def unique_count(string):
    unique = []
    for char in string:
        if char not in unique:
            if char == '\n':
                pass
            else:
                unique.append(char)
    return len(unique)
            
yes = np.zeros(len(data))
for ii in range(len(data)):
    yes[ii] = unique_count(data[ii])

print(np.sum(yes))

def everyone_yes(string):
    string = string.split()
    q_yes = string[0]
    for ii in range(1,len(string)):
        for char in q_yes:
            if char not in string[ii]:
                q_yes = q_yes.replace(char,"")
    return len(q_yes)

yes_2 = np.zeros(len(data))
for ii in range(len(data)):
    yes_2[ii] = everyone_yes(data[ii])

print(np.sum(yes_2))                




