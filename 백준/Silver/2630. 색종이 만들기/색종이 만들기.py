from sys import stdin

def make_s(arr, x, y, n):
    global white, blue
    color = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color: # 색 다르면 4등분
                make_s(arr, x, y, n // 2)
                make_s(arr, x, y + n // 2, n // 2)
                make_s(arr, x + n // 2, y, n // 2)
                make_s(arr, x + n // 2, y + n // 2, n // 2)
                return
    # 색이 모두 같으면 숫자 세어준다
    if color == 1:
        blue += 1
    else:
        white += 1

n = int(stdin.readline())
white = 0
blue = 0
square = []

for _ in range(n):
    square.append(list(map(int, stdin.readline().split())))

make_s(square, 0, 0, n)
print(str(white) + '\n' + str(blue))
