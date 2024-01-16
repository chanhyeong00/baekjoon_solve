from sys import stdin
n = int(stdin.readline())

a = list(map(int, stdin.readline().split())) # 0 = 큐, 1 = 스택
b = list(map(int, stdin.readline().split())) # i번쨰 자료구조에 들어있는 원소

m = int(stdin.readline()) # 삽입할 수열 길이
c = list(map(int, stdin.readline().split())) # 큐스텍에 삽입할 원소를 담은 c
 
# 스택은 넣은 애가 고대로 나오고, 큐는 원래 들어있던 애가 나옴
cnt = 0 # 큐의 개수

for i in range(n-1, -1, -1): # 답은 m개만 나옴
    if cnt >= m:
        break 
    if a[i] == 0:
        cnt += 1
        print(b[i], end=' ')
if m > cnt: # 넣는 애가 더 많으면 
    for j in range(m - cnt):
        print(c[j], end=' ')
print('\n')