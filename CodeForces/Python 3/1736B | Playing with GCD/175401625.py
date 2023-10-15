#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:38:25 2022
 
@author: brianahaneku
"""
 
def gcd(y,z):
    while(z):
       y, z = z, y % z
    return abs(y)
 
def solve():
    n=int(input())
    a=input().split()
    a=[int(x) for x in a]
    b=[a[0],a[0]]
    for i in range(1,n):
        x=b[-1]
        if x%a[i]:
            b[-1]=(x*a[i]/gcd(x,a[i]))
        b.append(a[i])
    
    for i in range(n):
        if gcd(b[i],b[i+1])!=a[i]:
            print('NO')
            return
    print('YES')
        
            
        
    
 
    
 
 
 
t=int(input())
for k in range(t):
    solve()