from sys import stdin
from collections import deque

input = stdin.readline
n, k = map(int, input().split())
# 이 문제는 bfs로 하는 게 효율적
# Dfs로 풀면 각 노드마다 3개씩 뻗어가고, 수가 커지면 너무 많은 노드가 생김
visited = [0] * 100001

queue = deque([(n, 0)])

answer = 0
while queue:

    node, time = queue.popleft()

    if node == k: 
        answer = time
        break
    if node < 0 or node > 100000: continue

    if not visited[node]:
        queue.append((node*2, time+1))
        queue.append((node+1, time+1))
        queue.append((node-1, time+1))

    visited[node] = 1

print(answer)