#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
 
 
def solve():
    n=int(input())
    s=input()
    a=s.split(' ')
    a=[int(x) for x in a]
    opt=float('inf')
    c=0
    for x in a:
        if x%2:
            c+=1
    if c%2==0:
        print(0)
        return
    for x in a:
        r=x%2
        y=x//2
        l=1
        while y%2==r:
            y//=2
            l+=1
        opt=min(opt,l)
    print(opt)
    return
 
t=int(input())
for _ in range(t):
    solve()