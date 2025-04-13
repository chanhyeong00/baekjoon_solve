from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
campus = []
for _ in range(n):
    ca = input()
    campus.append(ca)

visited = [[0] * m for _ in range(n)]
dxy = [(1,0), (-1,0), (0, -1), (0, 1)]
y, x = -1, -1
for i in range(n): # 도연이 위치 찾기
    for j in range(m):
        if campus[i][j] == 'I':
            y, x = i, j
            break
queue = deque([(y, x)])
answer = 0

while queue:
    y, x = queue.popleft()
    if not visited[y][x]:
        visited[y][x] = 1
        if campus[y][x] == 'P':
            answer += 1
        for i in range(4):
            ny, nx = y+dxy[i][0], x+dxy[i][1]
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx]\
            and campus[ny][nx] != 'X':
                queue.append((ny, nx))

print('TT' if answer==0 else answer)