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
        r=input()
        n=r[:r.index(' ')]
        k=int(r[r.index(' ')+1:])
        c=input('')
        d=input('')
        a=[]
        b=[]
        i=0
        ix=0
        while i<len(c):
            j=i
            while j<len(c) and c[j]!=' ':
                j+=1
            a.append((int(c[i:j]),ix))
            ix+=1
            j+=1
            i=j
        
        i=0
        while i<len(d):
            j=i
            while j<len(d) and d[j]!=' ':
                j+=1
            b.append(int(d[i:j]))
            j+=1
            i=j
        
        a.sort()
        
        res=k
        for x,y in a:
            if x<=res:
                res+=b[y]
        print(res)
    
        
 
    