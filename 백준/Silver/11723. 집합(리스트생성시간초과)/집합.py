import sys


read = sys.stdin.readline

m = int(read())
S = set()

for _ in range(m):
    order = list(map(str, read().split()))
    o = order[0]
    if len(order) == 2:
        x = int(order[1])
        if o == 'add':
            if x not in S:
                S.add(x)
        elif o == 'remove':
            if x in S:    
                S.remove(x)
        elif o == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif o == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)
    else:
        if o == 'all':
            S = set(range(1,21))
        elif o == 'empty':
            S = set()
