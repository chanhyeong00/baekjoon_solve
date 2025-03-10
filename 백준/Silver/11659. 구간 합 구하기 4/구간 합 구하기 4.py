import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [0] * (N + 1) # 0은 0으로
dp[1] = lst[0]

for i in range(2, N+1):
    dp[i] = dp[i-1] + lst[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
