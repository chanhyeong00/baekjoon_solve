# '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우'에 사용할 수 있는 알고리즘
# 점화식
# D_ab = min(D_ab, D_ak + D_kb) 로 최단거리를 구한다.


# 예시 코드(틀)
from sys import stdin

input = stdin.readline


n, B = map(int, input().split())

# 유저 리스트
users = [_ for _ in range(1, n+1)]
# 관계 리스트
connections = [[0 for _ in range(n)] for _ in range(n)]
# 관계의 케빈 베이컨 수를 저장할 리스트
graph = [[float('inf')] * n for _ in range(n)]

# 관계를 입력받는 모듈
for _ in range(B):
    con1, con2 = map(int, input().split())
    connections[con1-1][con2-1] = 1
    connections[con2-1][con1-1] = 1

# 그래프 가중치 구하기
for i in range(n):
    for j in range(n):
        if i == j: # 본인한테 오는 건 0
            graph[i][j] = 0
        elif connections[i][j]: # 그 외는 1(한칸 건너오기 가능)
            graph[i][j] = 1

# 케빈 베이컨수를 찾는 모듈
for k in range(n):
    for i in range(n):
        for j in range(n): # D_ab = min(D_ab, D_ak + D_kb)
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 답변을 구하는 수
bncon = float('inf')
answer = 0
for i in range(n):
    s = sum(graph[i][:]) 
    if bncon > s:
        bncon = s
        answer = i

print(answer + 1)
