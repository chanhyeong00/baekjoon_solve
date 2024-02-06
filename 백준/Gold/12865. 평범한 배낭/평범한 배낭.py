from sys import stdin
read = stdin.readline

n, k = map(int, read().split())
lst = [(0, 0)]
for _ in range(n):
    w, v = map(int, read().split())
    lst.append((w, v))

dp = [0] * (k+1) # 가치 테이블

for i in range(1, n+1): # 배낭에 넣을 물건 
    w_curr, v_curr = lst[i]
    for w in range(k, w_curr-1, -1): #배냥 용량을 줄여나가며
        dp[w] = max(dp[w], dp[w - w_curr] + v_curr)

print(dp[k])