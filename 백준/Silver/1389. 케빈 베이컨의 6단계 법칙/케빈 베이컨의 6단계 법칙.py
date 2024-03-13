from sys import stdin
from collections import deque
input = stdin.readline

friends = dict()
n, m = map(int, input().split())

for _ in range(m):
    f1, f2 = map(int, input().split())
    if f1 not in friends:
        friends[f1] = [f2]
    else:
        friends[f1].append(f2)
    if f2 not in friends:
        friends[f2] = [f1]
    else:
        friends[f2].append(f1)

answer = []
people = [i for i in range(1, n+1)]
for p1 in people: # 한명 기준 잡고
    num = 0 # 베이컨 수
    for p2 in people:
        if p1 != p2: # 다른 사람인 경우 이사람까지의 베이컨의 수 구함
            queue = deque([(p1, 0)])
            visited = [0] * (n+1)
            while queue:
                node, cnt = queue.popleft()
                if node == p2:
                    num += cnt
                    break
                if not visited[node]:                 
                    visited[node] = 1
                    for p3 in friends[node]:
                        queue.append((p3, cnt+1))
    answer.append((p1, num))
answer.sort(key=lambda x:[x[1], x[0]])
print(answer[0][0])