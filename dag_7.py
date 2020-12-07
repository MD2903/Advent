#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:22:33 2020

@author: martijn
"""

import numpy as np

data = np.loadtxt("/Users/martijn/Documents/Universiteit/Programmeren/advent/dag_7.txt",dtype = str,delimiter = '.\n')


def rule(string):
    containment = string.split(' contain ')
    numbercontained = containment[1].split(', ')
    x = [[None for _ in range(2)] for _ in range(len(numbercontained))]
    for ii in range(len(numbercontained)):
        x[ii][0] = numbercontained[ii][0]
        x[ii][1] = numbercontained[ii][2:numbercontained[ii].find('bag')+3]
    return [containment[0][:-1],x]  


#%%

check = -1
containee = ['shiny gold bag']
bags = []

while len(bags) != check:
    container = []
    check = len(bags)
    for ii in range(len(data)):
        for jj in range(len(containee)):
            rules = rule(data[ii])
            # print(containee, rules[1])
            for kk in range(len(rules[1])):
                if containee[jj] in rules[1][kk]:
                    if rules[0] in container:
                        pass
                    else:
                        container += [rules[0]]
                        bags += [rules[0]] 
    containee = container
        
print(len(set(bags)))

#%%

check = -1
container = [['1','shiny gold bag']]

totalbags = 0

while totalbags != check:
    check = totalbags
    for ii in range(len(data)):
        print(container,len(container))
        for jj in range(len(container)):
            rules = rule(data[ii])
            if container[jj][1] in rules[0]:
                n = int(container[jj][0])
                for kk in range(len(rules[1])):
                    if rules[1][kk][0] == 'n':
                        rules[1][kk][0] = 0
                    totalbags += n*int(rules[1][kk][0])
                    rules[1][kk][0] = n*int(rules[1][kk][0])
                container += rules[1]
                del container[jj]
    print(container,len(container))







