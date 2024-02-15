from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    if n == 1:
        print(1)
        continue  

    queue = deque([(idx, value) for idx, value in enumerate(lst)])

    cnt = 0
    while queue:
        max_ = max(queue, key=lambda x:x[1])
        e = queue.popleft()

        if e[1] == max_[1]:
            cnt += 1
            if e[0] == m:
                print(cnt)
                break
        else:
            queue.append(e)
