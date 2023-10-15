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
    a=input().split(' ')
    a=[int(x) for x in a]
    if len(a)==1:
        print("YES")
        print(str(a[0]))
        return
    if len(set(a))==1:
        print("NO")
        return
    a.sort()
    a=a[::-1]
    print("YES")
    i=1
    res=str(a[0])+' '+str(a[-1])
    while i<n-1:
        res+=' '+str(a[i])
        i+=1
        
    print(res)
    
    
    
        
    
    
        
    return
            
    
t=int(input())
for _ in range(t):
    solve()