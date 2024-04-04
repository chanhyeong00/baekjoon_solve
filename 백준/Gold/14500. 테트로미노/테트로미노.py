from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())

paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))


dxy = [(-1,0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, cnt, point):
    global answer
    if point + max_value*(4-cnt) <= answer:
        return
    if cnt == 4:
        answer = max(answer, point)
        return
    
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            # ㅓ, ㅜ, ㅗ, ㅏ
            if cnt == 2: # 이미 2개이고 nx, ny는 갔다고 생각하고 돌아가서 탐색
                visited[nx][ny] = 1
                dfs(x, y, cnt+1, point + paper[nx][ny])
                visited[nx][ny] = 0


            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, point+paper[nx][ny])
            visited[nx][ny] = 0

answer = -1
visited = [[0] * M for _ in range(N)]
max_value = max(map(max,paper))
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = 0
        
print(answer)
