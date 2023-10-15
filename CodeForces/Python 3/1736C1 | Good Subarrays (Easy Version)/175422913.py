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
    
    i=0
    j=0
    res=0
    while i<n:
        while j<n and a[j]>=j-i+1:
            j+=1
        res+=j-i
        i+=1
    print(res)
        
        
            
        
    
 
    
 
 
 
t=int(input())
for k in range(t):
    solve()