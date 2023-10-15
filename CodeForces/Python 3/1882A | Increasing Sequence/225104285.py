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
    n=int(input())
    a = list(map(int,input().split(" ")))
    s=set()
    used = set()
    
    ans = 1
    k=1
    for i in range(n):
        while k in used or k==a[i]:
            k+=1
        ans = k
        used.add(k)
        k+=1
        
    print(ans)
    return
    
        
    
    
            
    
    
t=int(input())    
for _ in range(t):
    solve()
 
#sys.stdout.flush()