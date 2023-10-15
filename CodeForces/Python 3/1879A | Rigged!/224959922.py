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
    a = []
    for _ in range(n):
        a.append(list(map(int,input().split(" "))))
    s,e = a[0]
    for a,b in a[1:]:
        if a>=s and b>=e:
            print('-1')
            return
    print(s)
    return
    
            
    
    
            
t=int(input())
for _ in range(t):
    solve()