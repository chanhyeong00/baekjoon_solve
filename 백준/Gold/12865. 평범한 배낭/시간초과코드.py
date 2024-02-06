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
    for w in range(k+1):
        if w + w_curr <= k:  # i번째 물건을 넣을 수 있다면
            dp[i][w+w_curr] = max(dp[i-1][w+w_curr], dp[i-1][w] + v_curr)
                # 그 물건을 넣었을 때의 가치, 이전에 그 무게까지 넣었던 물건의 가치와 비교해서 큰 값으로 업데이트 
        dp[i][w] = max(dp[i-1][w], dp[i][w]) # 이전값 가져옴
print(dp)
