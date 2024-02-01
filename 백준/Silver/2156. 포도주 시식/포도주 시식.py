from sys import stdin

n = int(stdin.readline())
grape = []
dp = [0] * n # 각 자리까지 마실 수 있는 포도주의 최대 양
for _ in range(n): 
    grape.append(int(stdin.readline()))

dp[0] = grape[0]
if n > 1:
    dp[1] = grape[0] + grape[1]

for i in range(2, n):
    dp[i] = max(grape[i] + grape[i-1] + dp[i-3],\
                grape[i] + dp[i-2], dp[i-1])

# 한 잔을 기준으로 
# 그 잔을 마시고 다음잔, 다다음잔 먹는 경우
# 그 잔을 마시고 다담잔 마시는 경우
# 그 잔 안 마시고 다음잔 먹는 경우로 총 3개
print(dp[n-1])
