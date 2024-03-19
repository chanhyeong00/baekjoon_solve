from sys import stdin

input = stdin.readline

t = int(input())

def find_keing(x, y):
    global answer

    a, b = x, 0 # a는 고정
    result = x
    while result <= M*N:

        b = (result % N) # 나머지 만큼 가는 거임
        if b == 0: b = N # 나누어 떨어진다면 마지막
        if b == y:
            answer = result
            return
        else:
            result += M
    return 

for _ in range(t):
    M, N, x, y = map(int, input().split())
    answer = -1
    find_keing(x, y)
    print(answer)