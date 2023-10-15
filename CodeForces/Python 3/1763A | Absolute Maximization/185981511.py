#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
 
 
def solve():
    n=int(input())
    a=input().split(' ')
    a=[int(x) for x in a]
    res=0
    h={}
    for i in range(len(a)):
        j=0
        v=a[i]
        while v>0:
            if v%2==1:
                h[j]=h.get(j,0)+1
            v//=2
            j+=1
    if not h:
        print(0)
        return
    k=max(h.keys())
    
    l=0
    s=0
    for i in range(k,-1,-1):
        if i in h:
            l+=2**(i)
            if h[i]==n:
                s+=2**(i)
    print(l-s)
            
    return 
 
t=int(input())
for _ in range(t):
    solve()