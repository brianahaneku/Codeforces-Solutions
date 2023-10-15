# This is a sample Python script.
 
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
from collections import defaultdict
 
def isSubstring(a,b):
    return b in a
 
def solve():
    n, m = list(map(int,input().split()))
    #x = list(map(int, input().split(' ')))
    x = input()
    s = input()
    ans = 0
    if isSubstring(x,s):
        print(0)
        return
    while len(x) <= 3 * m or ans < 3:
        if isSubstring(x,s):
            print(ans)
            return
        ans += 1
        x += x
    if isSubstring(x,s):
        print(ans)
        return
    print(-1)
 
if __name__ == '__main__':
    for t in range(int(input())):
        solve()