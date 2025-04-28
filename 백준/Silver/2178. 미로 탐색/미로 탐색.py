import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
miro = []
for _ in range(N):
    miro.append(input())

queue = deque([(0,0,1)])
visited = [[0]*M for _ in range(N)]
dxy = [(0,1), (0, -1), (1, 0), (-1, 0)]
answer = 0
while queue:
    x, y, dis = queue.popleft()
    if x == N-1 and y == M-1: 
        answer = dis
        break # 큐를 이용한 너비 탐색이므로 가장 빨리 찾은 게 정답
    for (dx, dy) in dxy:
        if 0<=x+dx<N and 0<=y+dy<M and miro[x+dx][y+dy]=='1' and not visited[x+dx][y+dy]:
            visited[x+dx][y+dy] = 1
            queue.append((x+dx, y+dy, dis+1))
print(answer)