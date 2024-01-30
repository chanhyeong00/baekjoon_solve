from sys import stdin

t = int(stdin.readline())

tri = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def dp_tri(n):
     while len(tri) < n:
        last_idx = len(tri) - 1
        tri.append(tri[last_idx-1] + tri[last_idx-2]) # 전전부터 2개 더한 거

for _ in range(t):
    n = int(stdin.readline())
    if n <= len(tri):
        print(tri[n-1])
        continue
    dp_tri(n)
    print(tri[n-1])