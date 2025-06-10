import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

map_ = []
dis_lst = [[0]*m for _ in range(n)]
for _ in range(n):
    map_.append(list(map(int, input().split())))

# 2 지점 먼저 찾기
dest_i, dest_j = 0, 0
for i in range(n):
    for j in range(m):
        if map_[i][j] == 2:
            dest_i, dest_j = i, j

# 2 지점부터 너비 우선 탐색으로 거리 찾기
dxy = [(0,1), (0, -1), (1, 0), (-1, 0)]
visited = [[0]*m for _ in range(n)]

queue = deque([(dest_i, dest_j, 0)])
visited[dest_i][dest_j] = 1
while queue:
    x, y, dis = queue.popleft()
    for (dx, dy) in dxy:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and map_[nx][ny] != 0:
            queue.append((nx, ny, dis+1))
            visited[nx][ny] = 1
            dis_lst[nx][ny] = dis + 1
        
# 확인 작업(지도에서 원래 0이면 0, 0이 아닌데 0이면 -1로)
for i in range(n):
    for j in range(m):
        # if map_[i][j] == 0:
        #     dis_lst[i][j] = 0
        if map_[i][j] !=0 and visited[i][j] == 0:
            dis_lst[i][j] = -1
for i in range(n):
    print(*dis_lst[i])