from sys import stdin
from collections import deque
n = int(stdin.readline())
cnt = 0

for i in range(1, 10): # 첫자리 정해줌
    dp = [0] * 10 # 0-9까지 개수
    dp[i] += 1
    for _ in range(n-1):# 둘째부터 n번째 자리까지
        lst = [0] * 10
        for num, d in enumerate(dp):
            if num == 0:
                lst[num + 1] += (1 * d)
            elif num == 9:
                lst[num - 1] += (1 * d)
            else:
                lst[num - 1] += (1 * d)
                lst[num + 1] += (1 * d)
        dp = lst
    
    cnt += (sum(dp))
print(cnt % 10**9)
