from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
A =[]
B = []

for _ in range(n):
    A.append(list(map(int, input().split())))

m, k = map(int, input().split())

for _ in range(m):
    B.append(list(map(int, input().split())))

C = [[0] * k for _ in range(n)]

for i in range(n):
    for h in range(k):
        for j in range(m):
            C[i][h] += (A[i][j] * B[j][h])

for i in range(n):
    for j in range(k):
        print(C[i][j], end=' ')
    print()