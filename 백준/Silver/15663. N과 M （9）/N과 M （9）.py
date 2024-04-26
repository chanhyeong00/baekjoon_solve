from sys import stdin
input = stdin.readline


N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

def dfs(k):
    if k == M:
        l = tuple(ls)
        answer.add(l)
        return
    
    for i in range(N):
        if not visited[i]:
            ls.append(lst[i])
            visited[i] = 1
            dfs(k+1)
            ls.pop()
            visited[i] = 0

answer = set()
visited = [0]*N
ls = []

dfs(0)
answer = sorted(answer)
for a in answer:
    print(*a)