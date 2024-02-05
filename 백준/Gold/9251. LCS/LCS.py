from sys import stdin

s1 = stdin.readline().strip()
s2 = stdin.readline().strip()

l1 = len(s1)
l2 = len(s2)

dp = [0] * l2

for i in range(l1): 
    prev = 0 # 이전 lcs 최대값
    for j in range(l2):
        if prev < dp[j]: # 최대값이면 저장
            prev = dp[j]
            continue
        if s1[i] == s2[j]: # 두 문자열이 같으면
            dp[j] = prev + 1 # 이전 최대 길이에서 1 늘림
print(max(dp))