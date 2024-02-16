from sys import stdin

input = stdin.readline

n, m, b = map(int, input().split())
region = []
avg = 0
mem = dict()

for _ in range(n):
    r = list(map(int, input().split()))
    avg += sum(r)
    region.append(r)

max_height = ((avg+b) // (n*m))

for i in range(n):
    for j in range(m):
        if region[i][j] not in mem:
            mem[region[i][j]] = 1
        else:
            mem[region[i][j]] += 1
lst = list(mem.items())
lst.sort(reverse=True, key=lambda x: [x[1], x[0]]) 

height, time = 0, float('inf')

for h in range(max_height, -1, -1):
    
    inv = b
    time_ = 0
    for l in lst: # 탐색
        if l[0] > h: # 더 높다면 빼야함
            need = l[0] - h
            inv += (need * l[1]) # 인벤에 저장
            time_ += (l[1] * need * 2)
        elif l[0] < h: # 낮으면 인벤에서 빼서 추가
            need = h - l[0]
            inv -= (need * l[1]) # 인벤에서 빼서 넣음
            time_ += (need * l[1])
    if inv >= 0 and time_ < time: # 인벤이 음수가 아니고 시간 짧으면 저장
        time = time_
        height = h

print(time, height)