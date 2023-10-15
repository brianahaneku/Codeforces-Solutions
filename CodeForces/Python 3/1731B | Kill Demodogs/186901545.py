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
    x=(n-1)*n*(n+1)//3+n*(n+1)*(2*n+1)//6
    x=x*2022
    x=x%(10**9+7)
    print(x)
    return
 
t=int(input())
for _ in range(t):
    solve()