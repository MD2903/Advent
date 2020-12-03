#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:30:25 2020

@author: martijn
"""
import numpy as np
from timeit import default_timer as timer

file = open('/Users/martijn/Documents/Universiteit/Programmeren/advent/dag_3.txt')

start = timer()

pattern = file.read().split()

slope = np.array([(1,1),(3,1),(5,1),(7,1),(1,2)])
trees = np.zeros(len(slope))

for ii in range(len(slope)):
    p = np.array([0,0]) 
    while p[1] < len(pattern) - 1:
    
        p = p + slope[ii]
    
        if p[0] > len(pattern[0]) - 1:
            p[0] -= len(pattern[0])
    
        if pattern[p[1]][p[0]] == '#':
            trees[ii] += 1

product = np.prod(trees)
            
end = timer()

print(end-start)

        
    


