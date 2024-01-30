from sys import stdin

n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))

num = 0
max_ = -float('inf')

for i in range(n):
    num = max(num+lst[i], lst[i]) # 누적합과 본인 중에 큰 걸로
    max_ = max(num, max_) # 최대값과 비교
print(max_)