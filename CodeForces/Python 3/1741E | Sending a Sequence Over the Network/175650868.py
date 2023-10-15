#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
 
 
def solve():
    n=int(input())
    b=input().split(' ')
    b=[int(x) for x in b]
    dp=[False for _ in range(n+1)]
    dp[-1]=True
    h={}
    for j in range(n):
        if j not in h:
            h[j]=[]
            
        if j-b[j]>=0:
            h[j-b[j]].append(j)
    for i in range(n-1,-1,-1):
        x=b[i]
        if x<=n-(i+1):
            dp[i]=dp[i] or dp[i+x+1]
        for j in h[i]:
            dp[i]=dp[i] or dp[j+1]
    if dp[0]:
        print('YES')
    else:
        print('NO')
 
 
t=int(input())
for _ in range(t):
    solve()