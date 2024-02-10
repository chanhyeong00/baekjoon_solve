from sys import stdin
read = stdin.readline

n, m = map(int, read().split())
lst = []

dp_row = [[0] * (n+1) for _ in range(n+1)]  # 행 별 누적합
dp_sq = [[0] * (n+1) for _ in range(n+1)] # 사각형 누적합


for _ in range(n):
    lst.append(list(map(int, read().split())))

for i in range(1, n+1): # 열에 대한 누적합 구하기
    for j in range(1, n+1):
        dp_row[i][j] = dp_row[i][j-1] + lst[i-1][j-1]


for i in range(1, n+1):  # 각 사각형 별 누적합
    for j in range(1, n+1):
        dp_sq[i][j] = dp_sq[i-1][j] + dp_row[i][j-1] + lst[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, read().split())
    print(dp_sq[x2][y2] - (dp_sq[x1-1][y2] + dp_sq[x2][y1-1] - dp_sq[x1-1][y1-1]))
    # 큰 사각형에서 뺴야하는 부분과 채워야 하는 부분 선택
