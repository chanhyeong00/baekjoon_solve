import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [1]*(N + 1)
arr[0], arr[1] = 0, 0
for i in range(2, int(N**(1/2)) + 1):
    if arr[i] == 0:
        continue
    for j in range(2*i, N+1, i):
        if arr[j] != 0:
            arr[j] = 0
for i in range(M, N+1):
    if arr[i] != 0:
        print(i)