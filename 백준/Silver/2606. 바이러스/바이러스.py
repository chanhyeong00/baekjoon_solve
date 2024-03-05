from sys import stdin
import sys
input = stdin.readline

n = int(input())
n_net = int(input())
connect = dict()

for _ in range(n_net):
    c1, c2 = map(int, input().split())
    if c1 not in connect:
        connect[c1] = {c2}
    else:
        connect[c1].add(c2)
    if c2 not in connect:
        connect[c2] = {c1}
    else:
        connect[c2].add(c1)

answer = 0
visited = [0] * (n+1)
visited[1] = 1
if 1 in connect:
    infect = [i for i in connect[1]]
else:
    infect = []
while infect:
    inf = infect.pop()
    if not visited[inf]:
        visited[inf] = 1
        answer += 1
        for j in connect[inf]:
            infect.append(j)

print(answer)
