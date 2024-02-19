from sys import stdin

input = stdin.readline

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
cnt = {-1: 0, 0: 0, 1: 0}


def check_same(row, col, k): # 숫자를 리턴하게해서 -1,0,1이면 수 리턴, 아니면 -2 리턴
    num = paper[row][col]
    for i in range(row, row+k):
        for j in range(col, col+k):
            if paper[i][j] != num:
                return False
    return True

def find_same(row, col, k):
    global cnt
    if check_same(row, col, k): # 모두 색이 같다면 
        cnt[paper[row][col]] += 1
        return
    else: # 다르면 9개로 자름
        m = k // 3
        move_row = [row, row+m, row+2*m]
        move_col = [col, col+m, col+2*m]
        for i in range(3):
            for j in range(3):
                find_same(move_row[i], move_col[j], m)
    return
find_same(0, 0, n)
for c in cnt.values():
    print(c)