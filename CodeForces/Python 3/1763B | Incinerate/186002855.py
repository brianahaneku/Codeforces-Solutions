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
    n,k=input().split(' ')
    n,k=int(n),int(k)
    h=input().split()
    p=input().split()
    a=[(int(p[i]),int(h[i])) for i in range(n)]
    a.sort()
    i=0
    
    lost=0
    while i<n:
        p,h=a[i]
        h-=lost
        if h<=0:
            i+=1
            continue
        if i>0:
            k-=p
        if k<=0:
            break
        sq = (1+2*k/p)**2 - 4*2*h/p
        b=1+2*k/p
        if sq<0:
            print('NO')
            return
        x=math.ceil((b-math.sqrt(sq))/2)
        
        if x<0:
            x=math.floor((b+math.sqrt(sq))/2)
            if x<0:
                print("NO")
                return
        lost+=k*x-x*(x-1)*p/2
        k-=(x-1)*p
        i+=1
    if i==n:
        print("YES")
    else:
        print("No")
 
        
        
    
            
    return 
 
t=int(input())
for _ in range(t):
    solve()