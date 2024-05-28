import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 하나 노드 기준으로 양쪽으로 가장 먼 애 찾기
def dfs(node, w):
    for next_node, next_w in tree[node]:
        if distance[next_node] == -1:
            distance[next_node] = w + next_w
            dfs(next_node, w + next_w)

n = int(input())
tree = {i: [] for i in range(1, n+1)}

for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))  # 양방향 트리로 구성

distance = [-1] * (n + 1)
distance[1] = 0 # 루트 노드
dfs(1, 0) # 루트 노드로부터 가장 먼 노드 찾음

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))