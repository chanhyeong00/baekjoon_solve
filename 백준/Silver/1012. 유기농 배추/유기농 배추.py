from sys import stdin
import sys
sys.setrecursionlimit(10**6) 
input = stdin.readline

t = int(input())

def check_move(x, y):
    if x < 0 or y < 0 or x >= m and y >=n:
        return

    if not visited[x][y] and ground[x][y] == 1:
        visited[x][y] = 1
        ground[x][y] = 0

        if x + 1 < m:
            check_move(x+1, y)
        if x - 1 >= 0:
            check_move(x-1, y)
        if y + 1 < n:
            check_move(x, y+1)
        if y - 1 >= 0:
            check_move(x, y-1)


for _ in range(t):
    m, n, k = map(int, input().split())
    ground = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1
    
    answer = 0
    # 이미 확인한 곳은 0으로 만들고, 오른쪽과 아래가 모두 0이면 찾음
    for i in range(m):
        for j in range(n):
            if ground[i][j] == 1:
                check_move(i, j)
                answer += 1
    print(answer)