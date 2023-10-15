#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
import sys
 
eps = 10**(-9)
M=10**9+7
 
 
prefix = [[0 for _ in range(30)] for _ in range(200003)]
 
# Python3 code for range maximum query and updates
from math import ceil, log
 
def solve():
    m = int(input())
    o=m
    
    a = list(map(int,input().split(" ")))
    
    #print(seg.compute(0,2))
    q=int(input())
    L=[]
    J=[]
    for ____ in range(q):
        l,j = list(map(int,input().split(" ")))
        L.append(l)
        J.append(j)
    
    
    
    for i,x in enumerate(a):
        j=0
        f=x
        for j in range(30):
            
            if a[i] & (1<<j):
                prefix[i+1][j] = 1 + prefix[i][j]
            else:
                prefix[i+1][j] = prefix[i][j]
 
    
    for y in range(q):
        l,j = L[y],J[y]
        if a[l-1] <j:
            if y!=q-1:
                print(-1,end =" ")
            else:
                print(-1)
            continue
        left = l-1
        right = o-1
        opt = -1
        while left<=right:
            mid = (left+right)//2
            v=0
            for r in range(30):
                if prefix[mid+1][r]-prefix[l-1][r]==mid-l+2:
                   v+=(1<<(r))
           
            if v>=j:
                left = mid+1
                opt = max(opt,mid+1)
            else:
                right = mid - 1
        if y!=q-1:
            print(opt, end = " ")
        else:
            print(opt)
        
            
    return
    
        
   
   
    
        
    
    
            
    
    
t=int(input())    
for _ in range(t):
    solve()
 
#sys.stdout.flush()