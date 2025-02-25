import sys 
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

_dict = {}
for c in cards:
    if c in _dict:
        _dict[c] += 1
    else:
        _dict[c] = 1

for ch in checks:
    if ch in _dict:
        print(_dict[ch], end=" ")
    else:
        print(0, end=" ")