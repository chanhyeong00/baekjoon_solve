from sys import stdin

input = stdin.readline

n = int(input())
k = int(input())

start, end = 1, n * n # 수는 1 부터 n*n까지 있음
answer = 0

while start <= end:
    mid = (start + end) // 2 # 절반 하고
    cnt = 0
    for i in range(1, n+1): # 중간지점까지 몇 개인지 카운트
        num = (mid // i)
        if num > n:
            cnt += n
        else:
            cnt += num

    if cnt >= k: # k보다 크거나 같으면 숫자를 줄여서 탐색(같은 숫자 여러개인 경우도 존재)
        end = mid-1
        answer = mid
    elif cnt < k: # 작다면 가능한 수의 크기 범위를 늘려서 탐색
        start = mid + 1
print(answer)