from sys import stdin

n = int(stdin.readline())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n): # 기준점
    for j in range(i):  # 그 기준을 삼아 왼쪽을 본다
        if arr[j] < arr[i]: # 기준보다 작으면 
            dp[i] = max(dp[i], dp[j] + 1) # 기준을 거쳐서 올 수 있다는 뜻이므로 기준에 +1

print(max(dp))
