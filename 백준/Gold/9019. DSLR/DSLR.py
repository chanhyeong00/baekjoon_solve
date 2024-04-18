from sys import stdin
from collections import deque
input = stdin.readline

    
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    queue = deque([(A, '')])
    anwer = 0

    while queue:
        a, order = queue.popleft()

        if a == B:
            answer = order
            break
        # D
        na = 2 * a
        if na > 9999: na %= 10000
        if not visited[na]:
            visited[na] = 1
            queue.append((na, order+'D'))
        
        # S
        if a == 0: na = 9999
        else: na = a - 1

        if not visited[na]:
            visited[na] = 1
            queue.append((na, order+'S'))      

        # L
        na = (a % 1000) * 10 + (a//1000)

        if not visited[na]:
            visited[na] = 1
            queue.append((na, order+'L'))
            
        # R
        na = (a%10) * 1000 + (a // 10)
        if not visited[na]:
            queue.append((na, order+'R'))
            visited[na] = 1

    print(answer)
