import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for g in graph.values():
    g.sort()

def dfs(v):
    if visited[v]: return
    print(str(v), end= ' ')
    visited[v] = 1
    for g in graph[v]:
        dfs(g)

def bfs(v):
    queue = deque([v])
    while queue:
        node = queue.popleft()
        if not visited[node]:
            print(str(node), end= ' ')
            for n in graph[node]:
                if not visited[n]:
                    queue.append(n)
        visited[node] = 1


visited = [0] * (N + 1)
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
print()