from sys import stdin

s1 = stdin.readline().strip()
s2 = stdin.readline().strip()

l1 = len(s1)
l2 = len(s2)

dp = [[0] * (l2+1) for _ in range(l1+1)] # s1 을 한 글자씩 s2 전체와 비교
# 초기값을 위해 +1 더 해준 것

for i in range(1, l1+1): # 
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]: # 두 문자열이 같으면
            dp[i][j] = dp[i-1][j-1] + 1 # 이전까지의 lcs 값에서 1을 늘림
        else: # 다른 경우는 이전까지의 lcs 최대값 저장(2가지 경우 -> 위, 왼쪽)
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
print(dp[-1][-1])
