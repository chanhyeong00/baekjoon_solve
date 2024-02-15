from sys import stdin
from collections import deque

input = stdin.readline

n,k = map(int, input().split())
coin = deque([])
for _ in range(n):
    coin.appendleft(int(input())) # 오름차순으로 받음

value = k
answer = 0
for c in coin:
    if c <= value:
       answer += (value // c)
       value -= (c * (value // c))
    if value == 0:
        break
print(answer)