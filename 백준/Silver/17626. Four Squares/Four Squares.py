from sys import stdin
import sys
sys.setrecursionlimit(100000)
input = stdin.readline

n = int(input())
answer = float('inf')
dp = [0] * (n+1) 

def find_min(n):
    if n <= 0:
        return 0
    if dp[n]:
        return dp[n] 
    else:    
        max_ = int(n**(1/2))
        m = n // max_**2
        dp[n] = m + find_min(n-(max_**2)*m)
        for i in range(max_-1, 0, -1):
            k = i ** 2 
            m = n // k
            dp[n] = min(dp[n], m + find_min(n-k*m))
    return dp[n]
print(find_min(n))