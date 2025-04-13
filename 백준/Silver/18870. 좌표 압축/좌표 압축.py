import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dic = {}

sort_lst = list(set(lst))
sort_lst.sort() # 크기순으로 정렬


for i in range(len(sort_lst)):
    dic[sort_lst[i]] = i

for j in lst:
    print(dic[j], end=" ")