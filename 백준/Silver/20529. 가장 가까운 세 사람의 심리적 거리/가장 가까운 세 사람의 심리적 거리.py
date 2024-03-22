from sys import stdin
input = stdin.readline

T = int(input())

def comp(a, b):
    r = 0
    for i in range(4):
        if lst[a][i] != lst[b][i]:
            r += 1
    return r

for _ in range(T):
    N = int(input())
    lst = list(map(str, input().split())) # 최대 16개 나옴
    if N > 32: 
    # 16개 칸에 2개씩 채워지고 1개가 들어오면 무조건 3개는 겹침
        print(0)
    else:
        answer = 1000
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1, N):
                    result = 0
                    result += comp(i, j)
                    result += comp(j, k)
                    result += comp(k, i)
                    answer = min(answer, result)
        print(answer)