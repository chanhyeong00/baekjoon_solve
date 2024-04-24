from sys import stdin
from collections import deque
input = stdin.readline


T = int(input())

for _ in range(T):
    n = int(input())
    score = []
    dp = [[0] * n for _ in range(2)]
    score.append(list(map(int, input().split())))
    score.append(list(map(int, input().split())))

    dp[0][0], dp[1][0] = score[0][0], score[1][0]
    if n >= 2:
        dp[0][1] = score[1][0] + score[0][1]
        dp[1][1] = score[0][0] + score[1][1]

    for j in range(2, n): 
        dp[0][j] = max(dp[0][j-2], dp[1][j-2], dp[1][j-1]) + score[0][j]
        dp[1][j] = max(dp[1][j-2], dp[0][j-2], dp[0][j-1]) + score[1][j]

    answer = max(max(dp[0]), max(dp[1]))
    print(answer)