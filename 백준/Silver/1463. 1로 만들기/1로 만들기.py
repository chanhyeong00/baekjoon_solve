from sys import stdin
n = int(stdin.readline())
dp = [0] * (n+1) # 각 수마다 연산횟수 저장

for i in range(2, n+1): # bottom-up
    dp[i] = dp[i-1] + 1 # +1 연산(초기화) 
    if i % 2 == 0: # *2 연산(2의 배수)
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0: # * 3 연산(3의 배수)
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])