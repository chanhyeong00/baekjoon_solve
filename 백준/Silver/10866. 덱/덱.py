import sys
from collections import deque
n = int(sys.stdin.readline())
d = deque([])
for _ in range(n):
     order = list(map(str, sys.stdin.readline().split()))
     if order[0] == 'push_front':
          d.appendleft(order[1])
     elif order[0] == 'push_back':
          d.append(order[1])
     elif order[0] == 'pop_front':
          if d:
               print(d.popleft())
          else:
               print(-1)
     elif order[0] == 'pop_back':
          if d:
               print(d.pop())
          else:
               print(-1)
     elif order[0] == 'size':
          print(len(d))
     elif order[0] == 'empty':
          if d: print(0)
          else: print(1)
     elif order[0] == 'front':
          if d: print(d[0])
          else: print(-1)
     elif order[0] == 'back':
          if d: print(d[-1])
          else: print(-1)