from sys import stdin
from collections import deque
input = stdin.readline


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(input()))

move = deque([(0,0,1)])
visited = [[0] * m for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0
while move:
    y, x, num = move.popleft()
    if y == n-1 and x == m-1:
        answer = num
        break

    if not visited[y][x]:
        visited[y][x] = 1
        for i in range(4):
            ny, nx = y+d[i][0], x+d[i][1]
            if 0<=ny<n and 0<=nx<m and maze[ny][nx] == '1':
                move.append((ny, nx, num+1))

print(answer)
