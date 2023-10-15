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
    #a = list(map(int,input().split(' ')))
    n = int(input())
    matrix = []
    for __ in range(n):
        matrix.append(input())
 
    st = 0
    ans = 0
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            l = []
            l.append(ord(matrix[n - 1 - j][i]))
            l.append(ord(matrix[n - 1 - i][n - j - 1]))
            l.append(ord(matrix[j][n - 1 - i]))
            l.append(ord(matrix[i][j]))
            x = max(l)
            for v in l:
                ans += x - v
    print(ans)
 
 
 
if __name__ == '__main__':
    for t in range(int(input())):
        solve()