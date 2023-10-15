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
    
    a,b,n = list(map(int,input().split(" ")))
    arr = list(map(int,input().split(" ")))
    
    ans = b-1
    b=1
    arr.sort()
    for x in arr:
        b = min(a,b+x)
        ans+=b-1
        b=1
    print(ans + 1)
    return
    
  
        
   
   
    
        
    
    
            
    
    
t=int(input())    
for _ in range(t):
    solve()
 
#sys.stdout.flush()