from sys import stdin

n = int(stdin.readline())
tri = []
dp = []

for i in range(n):
    tri.append(list(map(int, stdin.readline().split())))
    if i == 0: dp.append(tri[0])
    else: dp.append([0] *(i+1))

for i in range(1, n): # 층
    for j in range(i+1): # 이전값의 합 + 고정값
        if j == 0: dp[i][j] = dp[i-1][j] + tri[i][j] # 맨 왼쪽은 하나밖에 없음
        elif j == i: dp[i][j] = dp[i-1][j-1] + tri[i][j] # 맨 오른쪽도 하나밖에 없음
        else: dp[i][j] = max(dp[i-1][j] + tri[i][j], dp[i-1][j-1] + tri[i][j])
        # 나머지는 왼쪽 오른쪽 살펴서 최대값을 갱신
        # 그 층까지의 합중 최대값

print(max(dp[n-1]))


# 이것도 똑같이 마지막 값을 고정하고 
# 이전까지의 최대값 + 마지막값(고정시킨) 이라는 점화식으로 풀었음
