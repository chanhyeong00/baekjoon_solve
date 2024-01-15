import sys
i = 0 # 기준인 애 인덱스
n, k = map(int, sys.stdin.readline().split())
stack = [i for i in range(1,n+1)]

print('<', end='')
while stack: # 다 빠질 떄까지
    i += (k - 1)
    while i > (len(stack) - 1): #
        i -= (len(stack))
    if len(stack) == 1:
        print(stack.pop(), end='>\n')
        break
    print(stack.pop(i), end=', ')