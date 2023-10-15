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
    
    n,m=input().split(' ')
    n=int(n)
    m=int(m)
    a=input().split(' ')
    a=[int(x) for x in a]
    p=[0]
    ans=0
    mini=float('inf')
    for i in range(len(a)):
        
        p.append(a[i]+p[i])
       
        mini=min(mini,p[i+1])
    if p[m]==mini:
        print(ans)
        return
    z=[]
    accum=0
    
    for i in range(m+1,len(p)):
        if a[i-1]<0:
            a[i-1]=-a[i-1]
            heapq.heappush(z,-a[i-1])
        p[i]+=accum
        x=p[i]
        
        while x<p[m]:
            y=-heapq.heappop(z)
            x+=2*y
            ans+=1
            accum+=2*y
        p[i]=x
    
    if p[m]==min(p):
        print(ans)
        return
    z=[]
    for i in range(m-1,0,-1):
        if a[i]>0:
            a[i]=-a[i]
            heapq.heappush(z,a[i])
        while p[i]<p[m]:
            y=heapq.heappop(z)
            p[m]+=2*y
            ans+=1
    print(ans)
        
    return
            
    
t=int(input())
for _ in range(t):
    solve()