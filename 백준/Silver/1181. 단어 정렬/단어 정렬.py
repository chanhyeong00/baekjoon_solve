import sys
input = sys.stdin.readline


N = int(input())
lst = []
for i in range(N):
    lst.append(input().strip())


lst = list(set(lst)) # 중복 제거
lst.sort(key = lambda x:(len(x), x))

for l in lst:
    print(l)