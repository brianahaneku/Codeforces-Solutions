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
    
    n=int(input())
    a=input()
    f=False
    s=False
    for x in a:
        if x=='R':
            f=True
        if x=='L':
            s=f
    if s:
        print(0)
        return
    
    for i in range(n-1):
        if a[i]=='L' and a[i+1]=='R':
            print(i+1)
            return
    print(-1)
            
    
t=int(input())
for _ in range(t):
    solve()