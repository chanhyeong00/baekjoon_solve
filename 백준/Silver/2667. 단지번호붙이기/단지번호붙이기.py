import sys
input = sys.stdin.readline

N = int(input())
vil = []
for _ in range(N):
    vil.append(input())

visited = [[0]*N for _ in range(N)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
answer = []
for i in range(N):
    for j in range(N):
        cnt = 1
        if not visited[i][j] and vil[i][j] == '1':
            stack = [(i, j)]
            visited[i][j] = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in dxy:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<N and 0<=ny<N and vil[nx][ny] == '1' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        stack.append((nx, ny))
                        cnt += 1
            answer.append(cnt)
print(len(answer))
answer.sort()
for a in answer:
    print(a)
