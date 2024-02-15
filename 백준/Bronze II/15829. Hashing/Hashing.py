from sys import stdin
from collections import deque

input = stdin.readline

l = int(input())
str_ = input().strip()

hash_ = {chr(96+i):i for i in range(1, 27)}

answer = 0
i = 0
for a in str_:
    answer += (hash_[a] * (31 ** i))
    i += 1

print(answer)
