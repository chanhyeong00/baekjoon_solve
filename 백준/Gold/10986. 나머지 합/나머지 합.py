from sys import stdin
read = stdin.readline

n, m = map(int, read().split())

A = list(map(int, read().split()))

s = 0
dp = [0] * n
dp[0] = A[0] % m
remain = [0] * m # 나머지 표시
cnt = 0

for i in range(1, n): # 누적합의 나머지 구함
    dp[i] = (dp[i-1] + A[i]) % m # 0, 1, 2 중 하나

for i in range(n): # 나머지의 개수(0~m-1)
    remain[dp[i]] += 1

for i in range(m):
    if i == 0: # 누적합 나머지 0이면 하나만 있어도 나머지0
        cnt += remain[i]
# 다른 경우는 나머지 같은 것중 2개 뽑으면 된다(같은거끼리 뺴면 나머지 0)
# 즉, 나머지개수C2 인데  ->   나머지개수! / ((나머지개수-2)! * 2!)
#  (나머지개수 * 나머지개수-1 * ...) / ((나머지개수-2 * 나머지개수-3*...) * 2)
# = (나머지개수 * 나머지개수-1) // 2
    if remain[i] == 0: continue
    cnt += (remain[i] * (remain[i]-1) // 2)

print(cnt)
