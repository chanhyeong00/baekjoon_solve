import sys

N = int(input())
graph = []
connection = dict()
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    connection[i] = []
    for j in range(N):
        if graph[i][j] == 1:
            connection[i].append(j)
for i in range(N):
    visited = [0]*N
    stack = []
    start = i
    stack.append(i)
    while stack:
        node = stack.pop()
        for k in connection[node]:
            if not visited[k]:
                graph[start][k] = 1
                visited[k] = 1
                stack.append(k)
for g in graph:
    print(*g)
