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
    if n==1:
        print('1')
        return
    
    m=[[None for _ in range(n)] for __ in range(n)]
    l=2
    r=n*n
    f=True
    m[0][0]=1
    x=1
    directions=((0,1),(1,0),(0,-1),(-1,0))
    i=0
    j=1
    d=0
    dx,dy=directions[int(d)]
    while m[i][j] is None:
        if f:
            m[i][j]=r
            r-=1
            f=not f
        else:
            m[i][j]=l
            l+=1
            f=not f
        if (not 0<=i+dx<n) or (not 0<=j+dy<n) or m[i+dx][j+dy] is not None:
            d=int((d+1)%4)
            dx,dy=directions[int(d)]
        i,j=i+dx,j+dy
    for row in m:
        s=''
        for x in row:
            s+=' '+str(x)
        print(s[1:])
    
    
    
        
        
    return
            
    
t=int(input())
for _ in range(t):
    solve()