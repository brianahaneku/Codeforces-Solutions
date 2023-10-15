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
    a,b=input().split(' ')
    aL,bL=a[-1],b[-1]
    if aL=='L' and bL!='L':
        print('>')
        return
    if bL=='L' and aL!='L':
        print('<')
        return
    if aL=='S' and bL!='S':
        print('<')
        return
    if bL=='S' and aL!='S':
        print('>')
        return
    if aL=='M':
        print('=')
        return
    if len(a)==len(b):
        print('=')
        return
    if aL=='L':
        if len(a)>len(b):
            print('>')
        else:
            print('<')
        return
    if aL=='S':
        if len(a)>len(b):
            print('<')
        else:
            print('>')
    
    
    
t=int(input())
for _ in range(t):
    solve()
 
#t=int(input())
#for k in range(t):