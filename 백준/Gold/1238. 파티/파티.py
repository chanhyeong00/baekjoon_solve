import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(graph, start):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    heap = [(start, 0)]

    while heap: # X에서 출발할 때
        node, dist = hq.heappop(heap)

        if distance[node] < dist: # 이미 작다면 
            continue

        for n, d in graph[node]:
            new_dist = dist + d
            if new_dist < distance[n]:
                distance[n] = new_dist
                hq.heappush(heap, (n, new_dist))   
    return distance


N, M, X = map(int, input().split())
street = [[] for _ in range(N+1)] # 원래 길
reverse_street = [[] for _ in range(N+1)] # 방향이 반대인 길

for _ in range(M):
    start, end, t = map(int, input().split())
    street[start].append((end, t))
    reverse_street[end].append((start, t))

to_X = dijkstra(reverse_street, X) # X로 가는 최단 거리 구하기
from_X = dijkstra(street, X) # X에서 가는 최단 거리 구하기

max_distance = 0
for i in range(1, N+1):
    if to_X[i] != float('inf') and from_X[i] != float('inf'):
        max_distance = max(max_distance, to_X[i]+from_X[i])

print(max_distance)
    