import heapq
from sys import stdin
input = stdin.readline
n = int(input())
heap = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(heap) > 0:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -num)