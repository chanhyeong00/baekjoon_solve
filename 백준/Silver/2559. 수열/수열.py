from sys import stdin
read = stdin.readline

n, k = map(int, read().split())
temp = list(map(int, read().split()))

table = [0] * (n-k+1) # 시작점 기준 연속적인 합

for i in range(n-k+1):
    if i == 0: # 최조 누적합 계산
        for j in range(k):
            table[i] += temp[i+j]
    else:
        table[i] = table[i-1] - temp[i-1] + temp[i+k-1]
print(max(table))    
