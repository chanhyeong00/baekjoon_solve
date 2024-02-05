from sys import stdin
n = int(stdin.readline())
line = []
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    line.append((a, b))
line.sort(key=lambda x:x[0]) # 왼쪽 전깃줄에 대해 오름차순 정렬
# 전깃줄이 겹치지 않으려면 왼쪽 전깃줄을 정렬했을 때 오른쪽 전깃줄도 오름차순이어야함
# 그러므로 증가하는 부분 수열을 찾는 문제랑 같아짐
dp = [0] * n
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - (max(dp)+1))

