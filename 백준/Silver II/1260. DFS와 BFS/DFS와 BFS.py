from sys import stdin
from collections import deque

input = stdin.readline

n, m, v = map(int, input().split())
tree = {i:[] for i in range(1,n+1)}

for _ in range(m):
    node, conn = map(int, input().split())
    tree[node].append(conn)
    tree[conn].append(node)
    
for t in tree:
    tree[t].sort()

# 2 3 4   -> 2 
#  3 4   4
# 

def dfs(tree, node, queue, visited):
    if not visited[node-1]:
        visited[node-1] = 1
        print(node, end=' ')
        for t in tree[node]:
            dfs(tree,t, queue, visited)

def bfs(tree, v):
    queue = deque([v])
    visited = [0] * n
    while queue:
        vi = queue.popleft()
        
        if not visited[vi-1]:
            print(vi, end=' ')
            visited[vi-1] = 1

            for t in tree[vi]:
                queue.append(t)

queue = deque([v])
visited = [0] * n
dfs(tree, v, queue, visited)
print()
bfs(tree, v)
print()
