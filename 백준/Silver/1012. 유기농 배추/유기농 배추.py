import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    visited = [[0] * M for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and not visited[i][j]: # 배추가 심어져있고, 방문 안했으면
                stack = [(i, j)]
                while stack: # 너비 탐색으로 탐색 시작
                    y, x = stack.pop()
                    visited[y][x] = 1
                    if y + 1 < N and farm[y+1][x] == 1 and not visited[y+1][x]:
                        stack.append((y+1, x))
                    if x + 1 < M and farm[y][x+1] == 1 and not visited[y][x+1]:
                        stack.append((y, x+1))
                    if y - 1 >= 0 and farm[y-1][x] == 1 and not visited[y-1][x]:
                        stack.append((y-1, x))
                    if x - 1 >= 0 and farm[y][x-1] == 1 and not visited[y][x-1]:
                        stack.append((y, x-1))
                answer += 1
    print(answer)
                