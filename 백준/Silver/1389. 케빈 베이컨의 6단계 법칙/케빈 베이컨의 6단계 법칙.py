import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 연결 여부
connect = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    connect[x-1][y-1] = 1
    connect[y-1][x-1] = 1

# 케빈 베이컨 수 저장할 그래프
graph = [[float('inf')] * N for _ in range(N)]

# 직행 노선 구하기
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0
        else:
            if connect[i][j] == 1:
                graph[i][j] = 1

# 경유 노선 
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 답
bacon = float('inf')
answer = 0

for i in range(N):
    b = sum(graph[i])
    if b < bacon:
        answer= i
        bacon = b
print(answer+1)
