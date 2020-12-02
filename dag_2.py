#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:07:33 2020

@author: martijn
"""
import numpy as np
import re
from timeit import default_timer as timer

data = np.loadtxt("/Users/martijn/Documents/Universiteit/Programmeren/advent/dag_2.txt",dtype = str,delimiter = ":")

start = timer()

def criteria(string):
    n = re.findall(r'\d+', string)
    l = re.findall('[abcdefghijklmnopqrstuvwxyz]', string)
    return n+l

#%% 1

counter = 0
for ii in range(len(data)):
    if int(criteria(data[ii][0])[0]) <= data[ii][1].count(criteria(data[ii][0])[2]) <= int(criteria(data[ii][0])[1]):
        counter += 1
print(counter)    
  
#%% 2

counter = 0
for ii in range(len(data)):
    if (data[ii][1][int(criteria(data[ii][0])[0])] == criteria(data[ii][0])[2])^(data[ii][1][int(criteria(data[ii][0])[1])] == criteria(data[ii][0])[2]) == 1:
        counter += 1
print(counter)    

end = timer()
print(end-start)