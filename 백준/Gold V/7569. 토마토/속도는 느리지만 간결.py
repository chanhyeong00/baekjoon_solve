from sys import stdin
from collections import deque

input = stdin.readline

m, n, h = map(int, input().split())
top = []
for _ in range(h): # 3차원 배열
    tomato = []
    for _ in range(n):
        tomato.append(list(map(int, input().split())))
    top.append(tomato)

ripen = deque([])
num = 0
flag = False
for i in range(n):
    for j in range(m):
        for k in range(h): # 각 층마다 처음부터 익어있는 토마토
            if top[k][i][j] == 1:
                ripen.append((k,i,j))
                num += 1
            if top[k][i][j] == 0: # 안익은 거 있으면
                flag = True

if flag == False: # 다 익었다면
    print(0)
else:
    dx = [0,0,-1,1,0,0]
    dy = [0,0,0,0,-1,1]
    dz = [-1,1,0,0,0,0]
    days = 0
    while ripen:
        days += 1
        for _ in range(num): # 한 주기 돌 때가 하나
            (hgt, row, col) = ripen.popleft()
            for i in range(6):
                nh, nr, nc = hgt+dz[i], row+dy[i], col+dx[i]
                if(nh >= 0 and nh < h and nr >= 0 and nr < n and nc >= 0 and nc < m):
                    if top[nh][nr][nc] == 0: # 안 익었으면 익힘
                        ripen.append((nh,nr,nc))
                        top[nh][nr][nc] = 1

        num = len(ripen)
    for i in range(n):
        for j in range(m):
            for k in range(h): # 안익은 토마토 있는지
                if top[k][i][j] == 0:
                    print(-1)
                    exit(0)
    print(days-1)
