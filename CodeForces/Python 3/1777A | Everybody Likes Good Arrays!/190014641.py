#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
 
eps = 10**(-9)
 
# Python3 code for range maximum query and updates
from math import ceil, log
 
def solve():
    n=int(input())
    a=list(map(int,input().split(' ')))
    res=0
    for i in range(n-1):
        if a[i]%2==a[i+1]%2:
            res+=1
    print(res)
            
    
    
        
        
    return
            
    
t=int(input())
for _ in range(t):
    solve()