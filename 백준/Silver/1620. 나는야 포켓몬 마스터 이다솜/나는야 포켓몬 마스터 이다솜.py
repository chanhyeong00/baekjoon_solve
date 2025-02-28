import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict_ = {}

i = 1
for _ in range(N):
    name = input().strip('\n')
    dict_[name] = i
    dict_[str(i)] = name
    i += 1

for _ in range(M):
    order = input().strip('\n')
    print(dict_[order])