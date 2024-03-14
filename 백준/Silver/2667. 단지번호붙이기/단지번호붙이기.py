from sys import stdin
from collections import deque
input = stdin.readline


n = int(input())
vil = []
for _ in range(n):
    vil.append(list(input()))

visited = [[0] * n for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

house_num = 0
answer = []
num = 0 # 집 번호
while True:
    x, y = -1, -1
    flag = False
    for i in range(n): # 집을 찾는다.
        for j in range(n):
            if vil[i][j] == '1' and not visited[i][j]:
                y, x = i, j
                flag = True
                break
        if flag == True: break
    if flag == False: break # 찾을 집이 없음을 의미함
    # 집이 있다면 탐색 시작
    num += 1
    cnt = 0
    queue = deque([(y, x)]) # 좌표, 현재단지번호상태, 그곳 단지번호 
    while queue:
        y, x = queue.popleft()
        if not visited[y][x]:
            cnt += 1
            visited[y][x] = 1
            for i in range(4):
                ny, nx = y+d[i][0], x+d[i][1]
                if 0<=ny<n and 0<=nx<n and vil[ny][nx] == '1'\
                    and not visited[ny][nx]: # 단지 찾기
                        queue.append((ny, nx))
        
    answer.append(cnt)
answer.sort()
print(num)
for a in answer:
    print(a)
