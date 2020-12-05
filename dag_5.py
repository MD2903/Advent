#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:08:48 2020

@author: martijn
"""

import numpy as np
from timeit import default_timer as timer

data = np.loadtxt("/Users/martijn/Documents/Universiteit/Programmeren/advent/dag_5.txt",dtype = str)

start = timer()

def position(string):
    r_min = 0
    r_max = 127
    c_min = 0
    c_max = 7
    for ii in range(10):
        if string[ii] == 'F':
            r_max -= 64*2**(-ii)
        if string[ii] == 'B':
            r_min += 64*2**(-ii)
        if string[ii] == 'L':
            c_max -= 8*2**(6-ii)
        if string[ii] == 'R':
            c_min += 8*2**(6 -ii)
            
    return r_min*8+c_min

codes = np.zeros(len(data))
for jj in range(len(data)):
    codes[jj] = position(data[jj])

print(np.max(codes))

for ii in range(len(codes)):
    if codes[ii] + 1 not in codes and codes[ii]  + 2 in codes:
        print(codes[ii] + 1)
            
end = timer()

print(end-start)
    


        
        
            
    