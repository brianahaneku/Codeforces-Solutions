#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:08:20 2022
 
@author: brianahaneku
"""
import heapq
import math
 
eps = 10**(-9)
M=10**9+7
 
# Python3 code for range maximum query and updates
from math import ceil, log
 
def solve():
    n=int(input())
    nums=list(map(int, input().split(' ')))
    print(min(abs(nums[i]) for i in range(n)))
    
            
    
    
            
solve()
'''t=int(input())
for _ in range(t):
    solve()'''