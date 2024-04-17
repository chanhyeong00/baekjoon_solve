from sys import stdin
from collections import deque
input = stdin.readline

    
T = int(input())

for _ in range(T):
    A, B = map(str, input().split())
    visited = [0] * 10000
    queue = deque([('0'*(4-len(A))+A, '')])
    anwer = ''
    int_b = int(B)
    while queue:
        a, order = queue.popleft()
        int_a = int(a)

        if int_a == int_b:
            answer = order
            break
        # D
        na = 2 * int_a
        if na > 9999: na %= 10000
        if not visited[na]:
            visited[na] = 1
            na = str(na)
            queue.append(('0'*(4-len(na))+na,order+'D'))
    
            
        # S
        if int_a == 0: na = 9999
        else: na = int_a - 1

        if not visited[na]:
            visited[na] = 1
            na = str(na)
            queue.append(('0'*(4-len(na))+na, order+'S'))           

        # L
        na = []
        for i in range(1, 4):
            na.append(a[i])
        na.append(a[0])
        na = ''.join(na)
        int_na = int(na)

        if not visited[int_na]:
            queue.append((na, order+'L'))
            visited[int_na] = 1

        # R
        na = []
        na.append(a[-1])
        for i in range(3):
            na.append(a[i])

        na = ''.join(na)
        int_na = int(na)
        if not visited[int_na]:
            queue.append((na, order+'R'))
            visited[int_na] = 1

    print(answer)