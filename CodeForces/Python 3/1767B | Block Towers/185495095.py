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
    s=input()
    a=s.split(' ')
    res=int(a[0])
    a=[int(x) for x in a[1:]]
    
    heapq.heapify(a)
    while a:
        x=heapq.heappop(a)
        if x>res:
            res+=math.ceil((x-res)/2)
    
    print(res)
    return
 
t=int(input())
for _ in range(t):
    solve()