from sys import stdin
read = stdin.readline

n, m = map(int, read().split())
lst = list(map(int, read().split()))

table = [0] * (n+1)
table[0], table[1] = 0, lst[0]
for i in range(2, n+1):
    table[i] = lst[i-1] + table[i-1]
    
for _ in range(m):
    i, j = map(int, read().split())
    print(table[j] - table[i-1])