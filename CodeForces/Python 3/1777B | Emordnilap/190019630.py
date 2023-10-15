#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
 
eps = 10**(-9)
M=10**9+7
 
# Python3 code for range maximum query and updates
from math import ceil, log
 
def solve():
    n=int(input())
    if n==1:
        print(0)
        return
    res=0
    x=math.factorial(n-2)%M
    y=math.comb(n,2)%M
        
    for i in range(1,n):
        res=(res+((x*y)%M)*i)%M
    res=(res*2)%M
    res=(res+((x*n*(n-1))%M)*(n)*(n-1)//2)%M
    
            
    
    
        
        
    print(res)
            
    
t=int(input())
for _ in range(t):
    solve()