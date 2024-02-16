from sys import stdin

input = stdin.readline

n = int(input())
distances = list(map(int, input().split()))
oil = list(map(int, input().split()))

dp = [0] * n # 최소값 표시
min_ = 10 ** 9
for i in range(n):
    if oil[i] < min_:
        min_ = oil[i]
        dp[i] = min_
check = 0


answer = 0
min_ = 10 ** 9
for i in range(n-1):
    if dp[i] != 0:
        min_ = min(min_, dp[i])
    answer += (min_ * distances[i])
print(answer)