import sys
from collections import deque
n = int(sys.stdin.readline())
d = deque([])
for _ in range(n):
    order = list(map(int, sys.stdin.readline().split()))
    if len(order) == 1:
        if order[0] == 3:
            if d: 
                print(d.popleft())
            else:
                print(-1)
        elif order[0] == 4:
            if d: 
                print(d.pop())
            else:
                print(-1)     
        elif order[0] == 5:
            print(len(d))
        elif order[0] == 6:
            if d:
                print(0)
            else:
                print(1)
        elif order[0] == 7:
            if d:
                print(d[0])
            else:
                print(-1)
        elif order[0] == 8:
            if d:
                print(d[-1])
            else:
                print(-1)

    
    elif len(order) == 2:
        if order[0] == 1:
            d.appendleft(order[1])
        elif order[0] == 2:
            d.append(order[1])