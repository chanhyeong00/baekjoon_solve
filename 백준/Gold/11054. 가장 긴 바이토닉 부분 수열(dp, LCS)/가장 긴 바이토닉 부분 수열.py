from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
dp_left = [1] * n
dp_right = [1] * n
answer = 0 

for i in range(n): # 기준 i를 기준으로 왼쪽 방향으로 증가하는 수열의 최대길이 구하기 위함(완->오 감소)
    for j in range(i):
        if a[j] < a[i]:
            dp_left[i] = max(dp_left[i], dp_left[j]+1)
            # 기준에 따른 수열의 최대개수 계산
for i in range(n-1, -1, -1): # 기준 i를 기준으로 오른쪽 방향으로 증가하는 (오->왼 감소)
    for j in range(i, n):
        if a[j] < a[i]:
            dp_right[i] = max(dp_right[i], dp_right[j]+1)

for i in range(n):
    result = dp_left[i] + dp_right[i] - 1
    answer = max(answer, result)
print(answer) 
