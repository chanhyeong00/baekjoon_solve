from sys import stdin
import sys

input = stdin.readline

def z_move(s, x, y):
    global num

    if s==1:
        print(num)
        exit(0)
    else:
        term = (s//2) ** 2 # 4가지로 나눌 떄 번호 차이
        gap_x = x + s // 2
        gap_y = y + s // 2
        if r < gap_x: 
            if c < gap_y: # 1사
                z_move(s//2, x, y)
            else: # 2사
                num += term 
                z_move(s//2, x, gap_y)
  # 2사
        else:
            if c < gap_y: # 3사
                num += (2*term)
                z_move(s//2, gap_x, y)
            else: # 4사
                num += (3*term)
                z_move(s//2, gap_x, gap_y)
    return

    
n, r, c = map(int, input().split())
size = 2 ** n
num = 0 # 시작 번호(사각형 왼쪽 맨 위)
z_move(size, 0, 0)