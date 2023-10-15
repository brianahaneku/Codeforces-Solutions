#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:38:25 2022
 
@author: brianahaneku
"""
import math
 
 
def solve():
    
    #a=input().split(' ')
    n=int(input())
    res='1'
    for i in range(n,1,-1):
        res+=' '+str(i)
    print(res)
    
    
 
t=int(input())
for _ in range(t):
    solve()
 
#t=int(input())
#for k in range(t):