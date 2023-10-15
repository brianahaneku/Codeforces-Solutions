#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
 
eps = 10**(-9)
 
def solve():
    
    n,k=input().split()
    n,k=int(n),int(k)
    
    res=''
    a=[x for x in range(1,n+1)]
    
    i=0
    j=n-1
    for p in range(k-1):
        res+=' '+str(a[j])
        j-=1
    res+=' '+str(a[i])
    i+=1
    
    while i<=j:
        c=0
        while i<=j and c<k-1:
            res+= ' '+str(a[j])
            j-=1
            c+=1
        if i<=j:
            res+=' '+str(a[i])
            i+=1
   
    print(res[1:])
    
t=int(input())
for _ in range(t):
    solve()