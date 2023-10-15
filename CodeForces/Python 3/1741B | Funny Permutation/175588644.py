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
    if n==1 or n==3:
        print(-1)
        return
    res=''
    if n%2:
        for i in range(n//2):
            res+=str(n-i)+' '
        for i in range(n//2+1):
            res+=str(i+1)+' '
        print(res[:len(res)-1])
    else:
        for i in range(n,0,-1):
            res+=str(i)+' '
        print(res[:len(res)-1])
        
    
    
    
t=int(input())
for _ in range(t):
    solve()
 
#t=int(input())
#for k in range(t):