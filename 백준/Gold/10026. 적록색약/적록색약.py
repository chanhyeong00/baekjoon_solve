from sys import stdin
from collections import deque


input = stdin.readline

def find():
    k = 0
    for i in range(n): # 노드들 하나씩 탐색
        for j in range(n): 
            if not visited[i][j]: # 방문 x 노드라면 탐색시작
                stand = rgb[i][j]
                queue.add((i,j))
                while queue:
                    row, col = queue.pop()
                    visited[row][col] = 1
                    if row + 1 < n and not visited[row+1][col] and rgb[row+1][col] == stand:
                        queue.add((row+1, col)) # 밑에   
                    if col + 1 < n and not visited[row][col+1] and rgb[row][col+1] == stand: # 오른쪽
                        queue.add((row, col+1)) 
                    if row - 1 >= 0 and not visited[row-1][col] and rgb[row-1][col] == stand: # 위
                        queue.add((row-1, col)) 
                    if col - 1 >= 0 and not visited[row][col-1] and rgb[row][col-1] == stand: # 왼쪽
                        queue.add((row, col-1))
                k += 1
    return k

n = int(input())
rgb = []
visited = [[0] * 1000 for _ in range(1000)]
queue = set()

for _ in range(n):
    rgb.append(list(input().strip()))

result1 = find()

visited = [[0] * 1000 for _ in range(1000)]
for i in range(n):
    for j in range(n):
        if rgb[i][j] == 'G':
            rgb[i][j] = 'R'
result2 = find()

print(result1, result2)

