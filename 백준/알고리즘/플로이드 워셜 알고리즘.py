# '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우'에 사용할 수 있는 알고리즘
# 점화식
# D_ab = min(D_ab, D_ak + D_kb) 로 최단거리를 구한다.
# a-b 거리 = 직행노선과 경유 노선의 최소값

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

# 연결 되어있는지의 여부
for _ in range(B):
    con1, con2 = map(int, input().split())
    connections[con1-1][con2-1] = 1
    connections[con2-1][con1-1] = 1

# 그래프 가중치 구하기(직행 노선 구하기)
for i in range(n):
    for j in range(n):
        if i == j: # 본인한테 오는 건 0
            graph[i][j] = 0
        elif connections[i][j]: # 그 외는 1(한칸 건너오기 가능)
            graph[i][j] = 1

# 케빈 베이컨수를 찾기(경유 노선 포함해서 모든 최단거리 구하기)
for k in range(n): # 요것은 경유하는 놈(같은 행임)
    for i in range(n): # 각 행마다 하나씩 비교해봄
        for j in range(n): # D_ab = min(D_ab, D_ak + D_kb)
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 답변을 구하는 수
bncon = float('inf')
answer = 0
for i in range(n): # 1은 2까지의 거리부터 n 까지의 거리의 합, 2는 1,3,4,...n , ...
    s = sum(graph[i][:]) 
    if bncon > s:
        bncon = s
        answer = i

print(answer + 1)
