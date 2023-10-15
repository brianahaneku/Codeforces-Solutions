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
    s=input().split(' ')
    
    if int(s[0])==1:
        print('YES')
    else:
        print('NO')
    
    
    
 
t=int(input())
for _ in range(t):
    solve()
 
#t=int(input())
#for k in range(t):