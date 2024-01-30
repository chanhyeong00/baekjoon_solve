from sys import stdin

n = int(stdin.readline())
tri = []
dp = []

for i in range(n):
    tri.append(list(map(int, stdin.readline().split())))
    if i == 0: dp.append(tri[0])
    else: dp.append([0] *(i+1))

for i in range(1, n): # 층
    for j in range(i+1): # 이전값의 합 + 고정값
        if j == 0: dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == i: dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else: dp[i][j] = max(dp[i-1][j] + tri[i][j], dp[i-1][j-1] + tri[i][j])
        # 그 층까지의 합중 최대값

print(max(dp[n-1]))