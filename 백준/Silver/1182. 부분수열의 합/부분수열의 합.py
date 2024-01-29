from sys import stdin

def back(result, start):
    global answer
    if start >0 and result == s:
        answer += 1
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True # 기준 찾음
            back(result + lst[i], i+1)
            visited[i] = False

n, s = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
visited = [False] * n
answer = 0
back(0, 0)
print(answer)