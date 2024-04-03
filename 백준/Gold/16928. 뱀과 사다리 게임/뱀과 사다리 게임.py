from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())

ladders = []
snakes = []
visited = [0] * 101
for _ in range(N):
    ladders.append(list(map(int, input().split())))
for _ in range(M):
    snakes.append(list(map(int, input().split())))

def check_snake(p):
    for s in snakes:
        if s[0] == p:
            return s[1]
    return False

def check_ladder(p):
    for l in ladders:
        if l[0] == p:
            return l[1] # 있다면 사다리 타고
    return False # 없다면 그대로

queue = deque([(1,0)])
visited[1] = 1

answer = 0

while queue:
    point, cnt = queue.popleft()

    if point == 100:
        answer = cnt
        break
    
    for i in range(1, 7):
        np = point+i
        if np <= 100 and not visited[np]:
            while True:
                visited[np] = 1
                cs = check_snake(np)
                cl = check_ladder(np)             
                if cl: # cl값 존재하면
                    if cl == np: # 더이상 이동 x면 
                        break
                    np = cl
                elif cs: # cs값 존재하면
                    if cs == np: 
                        break
                    np = cs
                else: # 둘 다 없으면 탈출
                    break

                visited[np] = 1

            queue.append((np, cnt+1))

print(answer)