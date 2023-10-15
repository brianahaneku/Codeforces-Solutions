#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:38:25 2022
 
@author: brianahaneku
"""
import math
 
 
def solve():
    
    #a=input().split(' ')
    n,m=input().split()
    n,m=int(n),int(m)
    for _ in range(m):
        input()
    if m<n:
        print('Yes')
    else:
        print('NO')
    
    
    
 
t=int(input())
for _ in range(t):
    solve()
 
#t=int(input())
#for k in range(t):