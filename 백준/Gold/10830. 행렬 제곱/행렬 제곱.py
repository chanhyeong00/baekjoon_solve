from sys import stdin

input = stdin.readline
n, b = map(int, input().split())
A =[]
vector = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            vector[i][j] = 1

for _ in range(n):
    A.append(list(map(int, input().split())))

def metrix_pow(m, divide): # 거듭제곱
    if divide == 1: # 1제곱이면 m 반환
        return mul_metrix(m, vector)

    else: 
        new_m = metrix_pow(m, divide // 2) # 분할하고
        if divide % 2 == 0: # 짝수면 두 행렬끼리 곱함
            return mul_metrix(new_m, new_m)
        else: # 홀수면 두 행렬 곱하고 행렬 하나 더 곱함
            return mul_metrix(mul_metrix(new_m, new_m), A)
    
def mul_metrix(m1, m2): # 두 행렬 곱셈
    C = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for h in range(n):
            for j in range(n):
                C[i][h] = (C[i][h] + m1[i][j] * m2[j][h]) % 1000
    return C

answer = metrix_pow(A, b)
for an in answer:
    for a in an:
        print(a, end=' ')
    print() 