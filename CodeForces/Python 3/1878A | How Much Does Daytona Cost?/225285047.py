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
    b=list(map(int,input().split(" ")))
    n = b[0]
    k=b[1]
    a = list(map(int,input().split(" ")))
    if k in a:
        print("YES")
    else:
        print("NO")
    return
    
        
   
   
    
        
    
    
            
    
    
t=int(input())    
for _ in range(t):
    solve()
 
#sys.stdout.flush()