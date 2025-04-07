import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N + 1)
answer = 0
for i in range(1, N+1):
    if not visited[i]:
        stack = [i]
        while stack:
            x = stack.pop()
            if not visited[x]:
                visited[x] = 1
                for gx in graph[x]:
                    if not visited[gx]:
                        stack.append(gx)
        answer += 1
print(answer)