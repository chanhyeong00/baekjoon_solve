import sys
from collections import Counter

n = int(sys.stdin.readline())
num_lst = []
for _ in range(n):
    num = int(sys.stdin.readline())
    num_lst.append(num)
    
print(round(sum(num_lst) / n))

num_lst.sort()
print(num_lst[int(n/2)])
# most_common() 메쏘드는 등장한 횟수를 '내림차순'으로 정리
cnt_li = Counter(num_lst).most_common() # 예) (2, 3),(1, 3), (3, 2) ... -> 1 3개 , 2 3개..
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

print(max(num_lst) - min(num_lst))