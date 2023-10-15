#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
import sys
 
eps = 10**(-9)
M=10**9+7
 
# Python3 code for range maximum query and updates
from math import ceil, log
 
def solve():
    n = int(input())
    
    #a = list(map(int,input().split(" ")))
    ans = [1,3]
    k=5
    for _ in range(n-2):
        while (k*3)%(ans[-1]+ans[-2]) == 0:
            k+=1
        ans.append(k)
        k+=1
        
    print(' '.join([str(x) for x in ans]))
    return
    
        
   
   
    
        
    
    
            
    
    
t=int(input())    
for _ in range(t):
    solve()
 
#sys.stdout.flush()