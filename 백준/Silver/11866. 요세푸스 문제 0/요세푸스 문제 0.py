import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]
i = 0 # 기준
print('<', end='')
while lst:
    i += (k - 1)

    while len(lst) <= i:
        i -= len(lst)
    if len(lst) == 1:
        print(lst.pop(i), end='>')
    else:
        print(lst.pop(i), end=', ')