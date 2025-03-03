import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * (n + 1)

for i in range(1, n+1):
    stair[i] = int(input())

if n < 3: # 3개 미만이면 그냥 다 더한 값이 답
    print(sum(stair))
else:
    # dp 초기화
    dp = [0] * (n + 1)
    dp[1] = stair[1] 
    dp[2] = stair[1] + stair[2] # 2번째 계단은 이 방법 뿐
    dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])   # 1->3, 2->3 두가지

    for j in range(4, n+1):
        dp[j] = max(dp[j-3] + stair[j-1] + stair[j], dp[j-2] + stair[j])
    print(dp[n])


#  n번쨰 계단을 올라오는 법 점화식
#  1. n - 1 번째 계단을 밟고옴 -> n - 3을 밟아야만 함(3번 연속 못 밟음)
#  -> dp[n] = dp[n-3] + stair[n-1] + stair[n]
#  2. n - 2 번째를 밟고옴(이 경우는 n - 4를 밟는 겨우, n-3을 밟는 경우 모두 가능(초기화가 되어 더 아래꺼는 안 봐도 된다)
#  -> dp[n] = dp[n - 2] + stair[n]
# 이런식으로 bottom-up 방식으로 구현하려면 4부터 시작해야함(1번 케이스가 dp[n=3]) -> 그러므로 초깃값 설정 필요