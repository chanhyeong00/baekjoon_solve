from sys import stdin
import sys
input = stdin.readline

graph = dict()
node = set()
n, m = map(int, input().split())
visited = [0] * (n+1)
node = [i for i in range(1, n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = {v}
    else:
        graph[u].add(v)
    if v not in graph:
        graph[v] = {u}
    else:
        graph[v].add(u)

answer = 0

while node:
    start = node.pop()
    if not visited[start]:
        con_lst = [start]
        while con_lst:
            con = con_lst.pop()
            if not visited[con]:
                visited[con] = 1
                if con in graph:
                    for g in graph[con]:
                        con_lst.append(g)
        answer += 1
print(answer)