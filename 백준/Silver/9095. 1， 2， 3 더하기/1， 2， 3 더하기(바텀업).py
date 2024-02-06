from sys import stdin
read = stdin.readline
   
dp = [0] * (11)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
t = int(read())
for _ in range(t):
    print(dp[int(read())])
