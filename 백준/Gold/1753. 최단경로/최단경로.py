from sys import stdin
import heapq as hq
input = stdin.readline

V, E = map(int, input().split())
K = int(input()) # 시작 정점

tree = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    tree[u].append((w, v))


INF = float('inf')
distance = [INF] * (V+1) # 시작점에서 가는 거리
heap = []

hq.heappush(heap, (0, K)) # 힙큐에 튜플로 넣으면 첫 번째 원소 기준
distance[K] = 0
while heap:
    w, node = hq.heappop(heap)

    if distance[node] < w: # 이미 갱신된 거리가 더 짧으면 패스
        continue

    for next_w, next_node in tree[node]:
        new_w = w + next_w # 새로운 가중치
        if new_w < distance[next_node]: # 새로운 가중치가 갱신된 가중치보다 짧으면
            distance[next_node] = new_w # 새로 갱신
            hq.heappush(heap, (new_w, next_node))

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
