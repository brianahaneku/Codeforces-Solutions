# This is a sample Python script.
 
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
from collections import defaultdict
 
def isSubstring(a,b):
    return b in a
 
def solve():
    #n, m = list(map(int,input().split()))
    #x = list(map(int, input().split(' ')))
    #x = input()
    #s = input()
    a = list(map(int,input().split(' ')))
    a.sort()
    s = a[0]
    ct = 0
    for x in a[1:]:
        if x == 2*s:
            ct += 1
        elif x == 3*s:
            ct += 2
        elif x == 4 * s:
            ct += 3
        elif x == s:
            continue
        else:
            print("NO")
            return
    if ct <= 3:
        print("YES")
    else:
        print("NO")
'''
1 3 2
5 5 5
6 36 12
7 8 7
6 3 3
4 4 12
12 6 8
1000000000 1000000000 1000000000
3 7 1
9 9 1
9 3 6
2 8 2
5 3 10
8 4 8
2 8 4
'''
 
if __name__ == '__main__':
    for t in range(int(input())):
        solve()