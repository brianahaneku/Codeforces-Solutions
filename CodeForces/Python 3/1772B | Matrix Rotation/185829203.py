#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
 
 
def solve():
    matrix=[[0,0],[0,0]]
    s=input().split(' ')
    matrix[0]=[int(x) for x in s]
    s=input().split(' ')
    matrix[1]=[int(x) for x in s]
    if matrix[0][0]<matrix[0][1] and matrix[0][0]<matrix[1][0] and matrix[0][1]<matrix[1][1] and matrix[1][0]<matrix[1][1]:
        print("YES")
        return
    for i in range(3):
        new=[[0,0],[0,0]]
        new[0][0]=matrix[1][0]
        new[0][1]=matrix[0][0]
        new[1][1]=matrix[0][1]
        new[1][0]=matrix[1][1]
        matrix=new
        if matrix[0][0]<matrix[0][1] and matrix[0][0]<matrix[1][0] and matrix[0][1]<matrix[1][1] and matrix[1][0]<matrix[1][1]:
            print("YES")
            return
        
    print("NO")
    return
 
t=int(input())
for _ in range(t):
    solve()