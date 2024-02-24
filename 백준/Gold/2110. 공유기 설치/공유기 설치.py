from sys import stdin

input = stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
min_, max_ = 1, house[-1] - house[0] # 거리의 최소 최대
answer = 0

while min_ <= max_:
    mid = (max_ + min_) // 2 # 
    cnt = 1
    stand = house[0] # 첫 집 고정
    gap = 10 ** 9

    for i in range(1, n):
        if house[i] >= stand + mid:
            cnt += 1
            gap = min(gap, house[i]- stand)
            stand = house[i]
    if cnt < c: # 설치를 할 수 없다면(적게 설치되어서)줄여서 탐색
        max_ = mid - 1
    else: # 설치 가능하다면 늘려서도 탐색해봄
        min_ = mid + 1
        answer = gap
print(answer)