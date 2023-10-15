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
    if n==1:
        print("YES")
        print("1")
        return
    if n==3:
        print('NO')
        return
    print("YES")
    if (n%2==0):
        res=''
        for _ in range(n//2):
            res+='-1 1 '
        print(res[:-1])
        return
    else:
        b=n-1
        a=-(n-3)*b//(n-1)
        res=''
        for _ in range(n//2):
            res+=str(a)+' '+str(b)+' '
        res+=str(a)
        print(res)
        
    return
            
    
t=int(input())
for _ in range(t):
    solve()