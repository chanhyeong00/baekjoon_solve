from sys import stdin

input = stdin.readline

n = int(input())
video = []

def quad_zip(row, col, k):
    flag = True
    # 색상 다르면 다시 분할(4등분)
    color = video[row][col]
    for i in range(row, row+k):
        for j in range(col, col+k):
            if video[i][j] != color:
                flag = False
                break
    if flag == True:
        print(color, end='')
    else:
        print('(', end='')
        quad_zip(row, col, k//2)
        quad_zip(row, col+k//2, k//2)
        quad_zip(row+k//2, col, k//2)
        quad_zip(row+k//2, col+k//2, k//2)
        print(')', end='')
    return 
for _ in range(n):
    video.append(input())
quad_zip(0, 0, n)
print()