from sys import stdin

def fib_dp(n):
    global cnt
    for i in range(3, n+1):
        cnt += 1
        dp_lst[i] = dp_lst[i-1] + dp_lst[i-2]
    return dp_lst[n]

n = int(stdin.readline())

cnt = 0

dp_lst = [0] * 41
dp_lst[1] = 1
dp_lst[2] = 1
fib_dp(n)

print(dp_lst[n], cnt)