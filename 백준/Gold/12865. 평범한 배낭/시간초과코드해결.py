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
    if w_curr <= k:
        for w in range(k-w_curr+1):# w_curr - k까지
            dp[i][w+w_curr] = max(dp[i-1][w+w_curr], dp[i-1][w] + v_curr)
        for w in range(w_curr): # 나머지 업데이트
            dp[i][w] = dp[i-1][w]
    else: # 못 넣으면 이전값으로 다 업데이트
        for w in range(k+1):
            dp[i][w] = dp[i-1][w]


print(dp[n][k])
