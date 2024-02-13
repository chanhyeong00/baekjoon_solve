from sys import stdin
read = stdin.readline

n, m, k = map(int, read().split())
board = [read().strip() for _ in range(n)]

state_b = [[0] * (m+1) for _ in range(n+1)] # 칠해야하는 개수
state_w = [[0] * (m+1) for _ in range(n+1)]
min_ = float('INF')
# 체스판은 인덱스 합으로 구현 할 수 있음
for i in range(1, n+1): # 행 누적합
    for j in range(1, m+1):
        if (i-1 + j-1) % 2 == 0: 
            if board[i-1][j-1] == 'B': # 짝수지점 검정
                state_b[i][j] = state_b[i][j-1] # 검정시작인 애는 Ture
                state_w[i][j] = state_w[i][j-1] + 1 # 흰색 시작은 False
            else: # 짝수 지점 하얀색
                state_b[i][j] = state_b[i][j-1] + 1 # 검정 시작은 False
                state_w[i][j] = state_w[i][j-1] # 흰색 시작은 True 
        else:
            if board[i-1][j-1] == 'B': # 홀수지점 검정
                state_b[i][j] = state_b[i][j-1] + 1 # 검정 시작은 False 
                state_w[i][j] = state_w[i][j-1]
            else: # 홀수 지점 흰색
                state_b[i][j] = state_b[i][j-1]
                state_w[i][j] = state_w[i][j-1] + 1 #흰색 시작 False

for i in range(1, n+1): # 열 누적합
    for j in range(m+1):
        state_b[i][j] += state_b[i-1][j]
        state_w[i][j] += state_w[i-1][j]

# 최소값 구하기
for i in range(1, n-k+2):
    for j in range(1, m-k+2):
        b = state_b[i+k-1][j+k-1] - (state_b[i-1][j+k-1] + state_b[i+k-1][j-1]) + state_b[i-1][j-1]
        w = state_w[i+k-1][j+k-1] - (state_w[i-1][j+k-1] + state_w[i+k-1][j-1]) + state_w[i-1][j-1]
        min_ = min(b, w, min_)
print(min_)

    
