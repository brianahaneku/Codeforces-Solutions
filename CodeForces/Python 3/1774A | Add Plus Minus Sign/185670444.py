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
    a=input()
    
    res=''
    bit=True
    for i in range(1,len(a)):
        if a[i]=='1':
            if bit:
                res+='-'
            else:
                res+='+'
            bit = not bit
        else:
            res+='+'
    
    print(res)
    return
 
t=int(input())
for _ in range(t):
    solve()