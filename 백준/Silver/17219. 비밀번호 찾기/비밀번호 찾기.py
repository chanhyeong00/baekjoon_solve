from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
dict_ = {}

for _ in range(n):
    ad, pw = map(str, input().split())
    if ad not in dict_:
        dict_[ad] = pw

for _ in range(m):
    ad = input().strip()
    print(dict_[ad])