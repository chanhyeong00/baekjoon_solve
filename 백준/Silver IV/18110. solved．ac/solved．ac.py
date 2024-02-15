from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
op = list(int(input()) for _ in range(n))

op.sort()

def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

if n == 0:
    print(0)
else:
    e = round(n * 0.15)
    answer = 0
    for i in range(e, n-e):
        answer += op[i]
    print(round(answer / (n-(e*2))))