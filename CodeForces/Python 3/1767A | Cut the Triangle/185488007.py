#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
 
 
def solve():
    '''n=int(input())
    s=input()
    a=s.split(' ')
    a=[int(x) for x in a]'''
    input()
    points=[]
    for i in range(3):
        x,y=input().split(' ')
        points.append((int(x),int(y)))
    
    hor=False
    vert=False
    for i in range(2):
        for j in range(i+1,3):
            x,y=points[i]
            a,b=points[j]
            if y==b:
                hor=True
            if x==a:
                vert=True
    if hor and vert:
        print("NO")
    else:
        print("Yes")
    return
 
t=int(input())
for _ in range(t):
    solve()