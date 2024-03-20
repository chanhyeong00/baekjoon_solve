from sys import stdin
input = stdin.readline

N = int(input())

graph = [] # 그래프의 간선 상태
line = dict()

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    line[i] = []
    for j in range(N):
        if graph[i][j] == 1:
            line[i].append(j)

for i in range(N):
    start = i # 시작점
    stack = [] # 갈 수 있는 노드 리스트
    for k in line[i]:
        stack.append(k)
    while stack:
        end = stack.pop()
        graph[start][end]=1 # 갈 수 있는 노드임을 표시
        for k in line[end]:
            if graph[start][k] == 0: # 갔던 곳 아니면 넣기
               stack.append(k)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()