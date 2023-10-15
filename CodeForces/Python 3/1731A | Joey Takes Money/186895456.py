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
    a=input().split(' ')
    a=[int(x) for x in a]
    res=1
    for x in a:
        res*=x
    res+=len(a)-1
    res*=2022
    print(res)
    return        
 
t=int(input())
for _ in range(t):
    solve()