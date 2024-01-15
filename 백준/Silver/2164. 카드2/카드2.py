import sys
from collections import deque
n = int(sys.stdin.readline())
stack = deque([i for i in range(n, 0, -1)]) 
while len(stack) > 1:
    stack.pop()
    stack.appendleft(stack.pop())
print(stack[0])

