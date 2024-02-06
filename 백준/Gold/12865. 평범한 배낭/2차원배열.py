from sys import stdin
read = stdin.readline

n, k = map(int, read().split())
lst = [(0,0)]
for _ in range(n):
    w, v = map(int, read().split())
    lst.append((w,v))

dp = [[0]*(k+1) for _ in range(n+1)] # dp[n][w] # (물건을 n번쨰까지 넣음을 표시, 무게)

for i in range(1, n+1):
    w_curr, v_curr = lst[i]
    for w in range(k+1): # 해당 가방의 무게를 늘려가며
        if w >= w_curr: # 추가 되는 무게면
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_curr]+v_curr) 
          # 이전 값과 추가했을 때 값 비교
        else: # 추가 안 되면 이전 값과 같음
            dp[i][w] = dp[i-1][w]


print(dp[n][k])
