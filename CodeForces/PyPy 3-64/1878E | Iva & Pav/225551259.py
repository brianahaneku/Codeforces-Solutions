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
 
class SegmentTree():
    def __init__(self,arr):
        self.n = len(arr)//2
        self.tree = arr[::]
        #print(arr)
        self.build()
        #print(self.tree)
    
    def build(self):
        for i in range(self.n-1,0,-1):
            self.tree[i] = self.tree[i*2] & self.tree[i*2+1]
    
    def compute(self, l, r):
        l+=self.n
        r+=self.n
        ans = None
        #print(self.tree[l],self.tree[r])
        while l<=r:
            if l%2==1:
                if ans == None:
                    ans = self.tree[l]
                else:
                    ans&=self.tree[l]
                l+=1
            
            if r%2 == 0:
                if ans==None:
                    ans = self.tree[r]
                else:
                    ans&=self.tree[r]
                r-=1
            l//=2
            r//=2
        return ans
    
    def update(self,ix,val):
        ix+=self.n
        self.tree[ix] = val
        p=ix//2
        while p>0:
            self.tree[p] = self.tree[p*2] & self.tree[p*2+1]
            p//=2
    
            
 
# Python3 code for range maximum query and updates
from math import ceil, log
 
def solve():
    m = int(input())
    o=m
    
    a = list(map(int,input().split(" ")))
    k=1
    while k<m:
        k*=2
    while m<k:
        a.append(0)
        m+=1
    seg = SegmentTree([0]*k + a[::])
    #print(seg.compute(0,2))
    q=int(input())
    ret = []
    for __ in range(q):
        l,j = list(map(int,input().split(" ")))
        left = l-1
        right = o-1
        opt = -1
        while left<=right:
            mid = (left+right)//2
            v = seg.compute(l-1, mid)
            if v>=j:
                left = mid+1
                opt = max(opt,mid+1)
            else:
                right = mid - 1
        ret.append(opt)
            
    
    print(' '.join([str(x) for x in ret]))
    return
    
        
   
   
    
        
    
    
            
    
    
t=int(input())    
for _ in range(t):
    solve()
 
#sys.stdout.flush()