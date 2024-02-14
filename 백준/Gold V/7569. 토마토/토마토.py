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
    days = 0
    while ripen:
        days += 1
        for _ in range(num): # 한 주기 돌 때가 하나
            (hgt, row, col) = ripen.popleft()
            if hgt + 1 < h and top[hgt+1][row][col]!=1 and top[hgt+1][row][col] != -1:
                ripen.append((hgt+1, row, col))
                top[hgt+1][row][col] = 1
            if hgt - 1 >= 0 and top[hgt-1][row][col] != 1 and top[hgt-1][row][col] != -1:
                ripen.append((hgt-1, row, col))
                top[hgt-1][row][col] = 1
            if row + 1 < n and top[hgt][row+1][col] != 1 and top[hgt][row+1][col] != -1:
                ripen.append((hgt, row+1, col))
                top[hgt][row+1][col] = 1
            if row - 1 >= 0 and top[hgt][row-1][col] != 1 and top[hgt][row-1][col] != -1:
                ripen.append((hgt, row-1, col))
                top[hgt][row-1][col] = 1
            if col + 1 < m and top[hgt][row][col+1] != 1 and top[hgt][row][col+1] != -1:
                ripen.append((hgt, row, col+1))
                top[hgt][row][col+1] = 1
            if col - 1 >= 0 and top[hgt][row][col-1] != 1 and top[hgt][row][col-1] != -1:
                ripen.append((hgt, row, col-1))
                top[hgt][row][col-1] = 1
        num = len(ripen)
    flag = False
    for i in range(n):
        for j in range(m):
            for k in range(h): # 안익은 토마토 있는지
                if top[k][i][j] == 0:
                    flag = True
                    break
            if flag == True:
                break
        if flag == True:
            break
    
    print(-1 if flag == True else days-1)