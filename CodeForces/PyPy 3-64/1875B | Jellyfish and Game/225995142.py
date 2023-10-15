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
    
    m,n,k = list(map(int,input().split(" ")))
    j = list(map(int,input().split(" ")))
    g = list(map(int,input().split(" ")))
    s = sum(j)
    t = sum(g)
    l = None
    sm = None
    maxiG = max(g)
    miniJ = min(j)
    
    
    
    if maxiG>miniJ:
        s+=maxiG
        s-=miniJ
        t+=miniJ
        t-=maxiG
    k-=1
    if k>0:
        miniG = min(min(g),miniJ)
        maxiJ = max(max(j),maxiG)
        if maxiJ > miniG:
            t+=maxiJ
            t-=miniG
            s+=miniG
            s-=maxiJ
        k-=1
    if k%2 == 0 or k==0:
        print(s)
        return
 
    maxi = maxiJ
    mini = miniG
    print(s + maxi - mini)
    
    return
    
    
    
  
        
   
   
    
        
    
    
            
    
    
t=int(input())    
for _ in range(t):
    solve()
 
#sys.stdout.flush()