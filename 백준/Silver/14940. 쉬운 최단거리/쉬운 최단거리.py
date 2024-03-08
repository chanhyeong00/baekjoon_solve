from sys import stdin
from collections import deque

input = stdin.readline


n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    g = list(map(int, input().split()))
    graph.append(g)

# 목표를 찾고 인접노드부터 차례로 살핀다.
x, y = 0, 0 # 목표 지점 위치
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
            break
        
queue = deque([(x,y,0)])
distance = [[0] * m for _ in range(n)]

while queue:
    row, col, dist = queue.popleft()
    if row < 0 or row >= n or col < 0 or col >= m or \
        visited[row][col]: # 방문 했거나 인덱스 벗어나면
        continue
    
    if graph[row][col] != 0: # 방문 안했고 밟을 수 있는 땅이면
        queue.append((row-1, col, dist+1))
        queue.append((row+1, col, dist+1))
        queue.append((row, col-1, dist+1))
        queue.append((row, col+1, dist+1))
        # 거리 표시
        distance[row][col] = dist

    visited[row][col] = 1 # 방문했음

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] != 0:
            distance[i][j] = -1
for i in range(n):
    for j in range(m):
        print(distance[i][j], end=' ')
    print()