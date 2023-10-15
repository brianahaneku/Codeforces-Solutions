#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:37:54 2022
 
@author: brianahaneku
"""
 
if __name__=='__main__':
    INFTY=1000000005
    t=int(input())
    for tc in range(t):
        n=int(input())
        smallest=INFTY
        largest=-INFTY
        nums=input("")
        
        i=0
        j=0
        while i<len(nums):
            while j<len(nums) and nums[j]!=' ':
                j+=1
            smallest=min(smallest,int(nums[i:j]))
            largest=max(largest,int(nums[i:j]))
            i=j+1
            j+=1
        print(largest-smallest)
 
    