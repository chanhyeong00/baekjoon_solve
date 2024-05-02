from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())
queue = deque([(N, 0)])
visited = [0] * 100_001
while queue:
    loc, time = queue.popleft()
    if loc == K:
        print(time)
        break
    if loc > 100000 or loc < 0:
        continue
    if not visited[loc]:
        queue.append((loc*2, time))
        queue.append((loc-1, time+1))
        queue.append((loc+1, time+1))
        
    visited[loc] = 1
