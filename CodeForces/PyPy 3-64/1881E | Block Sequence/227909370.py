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
    dp = [float('inf') for _ in range(n + 1)]
    dp[-1] = 0
 
 
    for i in range(n - 1, -1, -1):
        dp[i] = 1 + dp[i + 1]
        if nums[i] > n - i - 1:
            dp[i] = min(dp[i], n - i)
        if i + nums[i] >= n:
            continue
        dp[i] = min(dp[i], dp[i + nums[i] + 1])
 
    print(dp[0])
 
 
 
 
if __name__ == '__main__':
    for t in range(int(input())):
        solve()