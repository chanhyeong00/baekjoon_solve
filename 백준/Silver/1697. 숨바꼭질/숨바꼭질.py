import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

answer = float('inf')
visited = [0] * 100_001
queue = deque([(N, 0)])

while queue:
    loc, time = queue.popleft()
    if loc == K:
        answer = time
        break
    if 0<=loc<=100_000 and not visited[loc]:
        visited[loc] = 1
        queue.append((loc*2, time+1))
        queue.append((loc+1, time+1))
        queue.append((loc-1, time+1))
    
print(answer)