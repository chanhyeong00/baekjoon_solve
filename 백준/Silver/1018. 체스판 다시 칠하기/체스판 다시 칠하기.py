import sys
m, n = map(int, sys.stdin.readline().split())
chess = []
cnt = []
for _ in range(m): # 체스판 입력
    pattern = sys.stdin.readline().strip()
    chess.append(pattern)

for i in range(m - 7): # ex) m= 9 면 0,1 로 시작할 때만 8x8 사각형 만들 수 있음
    for j in range(n - 7): # 8 * 8 정사각형 만들기 위함
        w_draw = 0
        b_draw = 0
        for a in range(i, i+8): # 8 x 8
            for b in range(j, j+8):
                if (a + b) % 2 == 0: # 짝수인 경우
                    if chess[a][b] != "W": # B이면(0~)
                        w_draw += 1
                    else: # W일 떄
                        b_draw += 1
                else: # 홀수
                    if chess[a][b] != "W": # B이면(0~)
                        b_draw += 1 # b로 칠하는 개수
                    else: # W일 떄
                        w_draw += 1 # w로 칠하는 개수
        cnt.append(w_draw)
        cnt.append(b_draw)
print(min(cnt))
