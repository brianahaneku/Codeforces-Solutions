#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:38:25 2022
 
@author: brianahaneku
"""
import math
 
class Node():
    def __init__(self,left=None,right=None,h=0,s=0):
        self.left=left
        self.right=right
        self.h=h
        self.s=s
 
def solve():
    n=int(input())
    s=input()
    
    res=1
    i=1
    st=0
    while i<n:
        if s[i]==s[i-1]:
            res=max(res,(i-st+1)**2)
        else:
            st=i
        i+=1
    
    c0=0
    for x in s:
        if x=='0':
            c0+=1
    res=max(res,c0*(n-c0))
    print(res)
    
    
    
 
t=int(input())
for _ in range(t):
    solve()
 
#t=int(input())
#for k in range(t):