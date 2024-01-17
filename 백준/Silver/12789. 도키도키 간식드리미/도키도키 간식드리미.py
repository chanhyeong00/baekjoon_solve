from sys import stdin
from collections import deque
n = int(stdin.readline())
curr_num = 1
current = deque(list(map(int, stdin.readline().split())))
wait_stack = []
while current:
     if current[0] == curr_num:
          current.popleft()
          curr_num += 1
     elif wait_stack and wait_stack[-1] == curr_num:
          wait_stack.pop(-1)
          curr_num += 1
     else:
          wait_stack.append(current.popleft())
          
for _ in range(len(wait_stack)):
     if curr_num == wait_stack[-1]:
          wait_stack.pop(-1)
          curr_num += 1

if curr_num == n+1:
     print('Nice')
else:
     print('Sad')
         