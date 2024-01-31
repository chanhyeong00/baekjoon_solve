from sys import stdin
from collections import deque
n = int(stdin.readline())
cnt = 0

# 결과 값은 맨앞높 고정시키고 계산(0과 9의 개수가 중요)
# 처음엔 무조건 2
# 그 이후론 0이나 9 가 나오면 이전자리 cnt + (cnt-0과9의수)로 계속 쌓아가는 방법
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