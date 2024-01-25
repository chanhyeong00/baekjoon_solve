from sys import stdin

def find_team(start, n, k):
    global answer
    if k == n // 2: # 이때 점수 차이 계산
        score_t1, score_t2 = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    score_t1 += (skills[i][j] + skills[j][i])
                elif not visited[i] and not visited[j] :  
                    score_t2 += (skills[i][j] + skills[j][i])
        answer = min(answer, abs(score_t1 - score_t2))
        return
    
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            find_team(i + 1 , n, k + 1) # 이미 본 거는 보지 않도록
            visited[i] = False

n = int(stdin.readline())
skills = []
for _ in range(n):
    skills.append(list(map(int, stdin.readline().split())))

visited = [False] * n
answer = 101
find_team(0, n, 0)
print(answer)

