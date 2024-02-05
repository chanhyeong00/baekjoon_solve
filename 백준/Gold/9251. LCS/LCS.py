from sys import stdin

s1 = stdin.readline().strip()
s2 = stdin.readline().strip()

l1 = len(s1)
l2 = len(s2)

dp1 = [0 for _ in range(l2+1)] # lcs 길이 기록
dp2 = [0 for _ in range(l2+1)]

for i in range(l1): # 
    dp2 = dp1.copy()
    for j in range(1, l2+1):
        if s1[i] == s2[j-1]: # 두 문자열이 같으면
            dp1[j] = dp2[j-1] + 1 # 이전까지의 lcs 값에서 1을 늘림
        else: # 다르면 이전값 저장
            dp1[j] = max(dp1[j-1], dp1[j])
    #dp2 = dp1 # 참조하기 때문에 쓰지말기
print(dp1[-1])