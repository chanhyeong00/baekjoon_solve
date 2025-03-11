import sys
input = sys.stdin.readline

n = int(input())
max_sqrt = int((n**(1/2)))

dp = [i for i in range(n+1)] # 모두 1^2으로 구성되는 최악의 상황으로 초기화

for i in range(2, n+1):
    for j in range(1, int(i**(1/2))+1):
        dp[i] = min(1 + dp[i-j**2], dp[i])

print(dp[n])

# dp[1] = 1
# dp[2] = dp[1] + dp[1]
# dp[3] = dp[1] + dp[2]
# dp[4] = 1
# dp[5] = dp[4] + dp[1]
# dp[6] = dp[4] + dp[2]
# dp[7] = dp[4] + dp[3]
# dp[n] = dp[i*i] + dp[n-i*i] (dp[i^2]은 항상 1)