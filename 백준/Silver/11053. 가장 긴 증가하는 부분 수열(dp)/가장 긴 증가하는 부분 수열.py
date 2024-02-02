from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
dp = [1] * n

for i in range(n): # 기준을 잡고
    for j in range(i+1, n): # 가면서 비교
        if a[i] < a[j]:
            dp[j] = max(dp[j], dp[i]+1)
            
print(max(dp))
