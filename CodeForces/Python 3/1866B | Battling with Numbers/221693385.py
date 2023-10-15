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
    primes=list(map(int, input().split(' ')))
    exp=list(map(int, input().split(' ')))
    x={}
    for i in range(n):
        x[primes[i]]=exp[i]
    
    m=int(input())
    primes=list(map(int, input().split(' ')))
    exp=list(map(int, input().split(' ')))
    y={}
    for i in range(m):
        y[primes[i]]=exp[i]
        if (primes[i] not in x) or exp[i]>x[primes[i]]:
            print(0)
            return
    
    
    res=1
    
    for v in x:
        expX=x[v]
        expY=y.get(v,0)
        if expX!=expY:
            res=(res*2)%998244353
    print(res)
    
            
    
    
            
solve()
'''t=int(input())
for _ in range(t):
    solve()'''