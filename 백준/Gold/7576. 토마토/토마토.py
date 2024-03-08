from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split()) # 열과 행
tomato = []
visited = [[0] * n for _ in range(m)]

for _ in range(m):
    t = list(map(int, input().split()))
    tomato.append(t)

queue = deque([])
check = False
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append((i, j, 0)) # 좌표, 시간
        if tomato[i][j] == 0:
            check = True # 안 익은 애 있는지 확인

if check == True: # 안 익은 애 있다면
    w = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    answer = -1
    while queue:
        row, col, time = queue.popleft()

        if  row < 0 or row >=m or col < 0 or col >=n or \
            visited[row][col] or tomato[row][col]==-1:
            continue

        answer = time
        for i in range(4):
            dy, dx = w[i]
            queue.append((row+dy, col+dx, time+1))
        visited[row][col] = 1

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and tomato[i][j]==0: # 익지 않은 토마토를 방문하지 않았다면
                answer = -1
                break
    print(answer)
else:
    print(0)