#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:53:24 2020

@author: martijn
"""

import numpy as np
from timeit import default_timer as timer

data = np.loadtxt("/Users/martijn/Documents/Universiteit/Programmeren/advent/dag_1_1.csv",dtype = int ,delimiter = ",")

start = timer()

som = np.zeros((200,200))

for ii in range(len(data)):
    for jj in range(1+ii,len(data)):  
        som[ii,jj] = data[ii] + data[jj]    
        if som[ii,jj] == 2020: 
            print(data[ii]*data[jj])
            print(ii,jj)
            break
    if som[ii,jj] == 2020:  
        break

# som = np.zeros((200,200,200))

# for ii in range(len(data)):
#     for jj in range(1+ii,len(data)):  
#         for kk in range(1+jj,len(data)):
#             som[ii,jj,kk] = data[ii] + data[jj] + data[kk]  
#             if som[ii,jj,kk] == 2020: 
#                 print(data[ii]*data[jj]*data[kk])
#                 break
#         if som[ii,jj,kk] == 2020:  
#             break  
#     if som[ii,jj,kk] == 2020:  
#         break  

end = timer()
             
print(end - start)