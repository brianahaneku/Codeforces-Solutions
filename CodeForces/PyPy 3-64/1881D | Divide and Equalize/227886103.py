# This is a sample Python script.
 
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
from collections import defaultdict
import math
 
 
def primeFactors(n, freq):
    while n % 2 == 0:
        n = n // 2
        freq[2] += 1
 
    for i in range(3, int(math.sqrt(n)) + 1, 2):
 
        # while i divides n , print i and divide n
        while n % i == 0:
            n = n // i
            freq[i] += 1
    if n > 2:
        freq[n] += 1
 
def solve():
    #n, m = list(map(int,input().split()))
    #x = list(map(int, input().split(' ')))
    #x = input()
    #s = input()
    #nums = list(map(int,input().split(' ')))
    n = int(input())
    nums = list(map(int, input().split(' ')))
    freq = defaultdict(int)
    for x in nums:
        primeFactors(x, freq)
 
    #print(freq)
    for key in freq:
        if freq[key] % n:
            print("NO")
            return
    print("YES")
 
 
 
if __name__ == '__main__':
    for t in range(int(input())):
        solve()