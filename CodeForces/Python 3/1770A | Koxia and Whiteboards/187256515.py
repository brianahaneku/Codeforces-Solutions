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
    n,m=input().split()
    n=int(n)
    m=int(m)
    a=input().split()
    b=input().split()
    a=[int(x) for x in a]
    b=[int(x) for x in b]
    heapq.heapify(a)
    for x in b:
        heapq.heappop(a)
        heapq.heappush(a, x)
    print(sum(a))
    return
    
t=int(input())
for _ in range(t):
    solve()